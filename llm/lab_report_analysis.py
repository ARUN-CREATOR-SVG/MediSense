from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from llm.utils import df_to_text
import pandas as pd
import os
import logging

load_dotenv()
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/llm", tags=["LLM"])

# Loading LLM model
model = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=800,
    temperature=0.1
)
llm = ChatHuggingFace(llm=model)

# Prompt Templates

healthy_prompt_template = PromptTemplate.from_template("""
You are an AI medical assistant. Analyze the patient's lab results and prediction below:

Prediction: {prediction}  
Risk Score: {risk_score}  

Lab Summary:  
{lab_data}  

Provide the following two sections clearly. Keep the tone helpful and simple.

1. **Explanation**  
Write 2–4 short sentences explaining what the lab results and prediction indicate in patient-friendly terms.

2. **Prevention Tips**  
List 5–7 clear and specific suggestions to maintain or improve liver health.  
**Each tip should be on a new line, using dash `-` as a bullet point.**  
Do not repeat or explain tips in long paragraphs.  
""")


unhealthy_prompt_template = PromptTemplate.from_template("""
You are an AI medical assistant. Analyze the patient's lab results and prediction below:

Prediction: {prediction}  
Risk Score: {risk_score}  

Lab Summary:  
{lab_data}  

Provide the following three sections. Use bullet points as described, and keep the tone clear and to the point.

1. **Explanation**  
Write 2–4 concise sentences summarizing the meaning of the lab results and risk score.

2. **Possible Causes**  
List 4–6 likely medical or lifestyle causes.  
Use this format:
- Cause one  
- Cause two  
...

3. **Prevention Tips**  
List 5–7 practical suggestions to reduce or manage the condition.  
Use this format:
- Tip one  
- Tip two  
...

Avoid repeating causes as tips. Each bullet must be short and on a new line.
""")



def select_prompt(risk_score: float):
    if risk_score <= 0.25:
        return healthy_prompt_template
    else:
        return unhealthy_prompt_template


# Request schema for LLM 
class LLMRequest(BaseModel):
    prediction: str = Field(..., example="Liver Disease")
    risk_score: float = Field(..., example=0.89)
    input_data: dict = Field(..., example={
        "age": 56,
        "bilirubin": 3.2,
        "albumin": 2.5
    })

@router.post("/lab-report-analyze")
def analyze_with_llm(data: LLMRequest):
    try:
        df = pd.DataFrame([data.input_data])
        lab_data_summary = df_to_text(df)

        selected_prompt = select_prompt( data.risk_score)

        parser = StrOutputParser()
        chain = selected_prompt | llm | parser

        response = chain.invoke({
            "prediction": data.prediction,
            "risk_score": data.risk_score,
            "lab_data": lab_data_summary
        })

        return {"response": response.strip()}

    except Exception as e:
        logger.exception("LLM error")
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")
