import requests

def get_llm_analysis(prediction, risk_score, input_data):
    url = "https://medisense-ai.onrender.com/llm/lab-report-analyze"
    payload = {
        "prediction": prediction,
        "risk_score": risk_score,
        "input_data": input_data
    }
    try:
        res = requests.post(url, json=payload)
        if res.status_code == 200:
            return res.json().get("response", "No response from LLM.")
        else:
            return f"Error from LLM API: {res.status_code}"
    except Exception as e:
        return f"Exception during LLM API call: {str(e)}"
