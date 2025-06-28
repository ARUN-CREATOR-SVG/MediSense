from pydantic import BaseModel,Field
from typing import Annotated

class HeartDiseaseForm(BaseModel):
    age: float = Field(..., alias="age", gt=0, example=52)
    sex: int = Field(..., alias="sex", example=1)
    chest_pain_type: int = Field(..., alias="Chest pain type", ge=0, le=3, example=0)
    bp: float = Field(..., alias="BP", gt=0, example=125)
    cholesterol: float = Field(..., alias="Cholesterol", gt=0, example=212)
    fbs_over_120: int = Field(..., alias="FBS over 120", ge=0, le=1, example=0)
    ekg_results: int = Field(..., alias="EKG results", ge=0, le=2, example=1)
    max_hr: float = Field(..., alias="MAX HR", gt=0, example=168)
    exercise_angina: int = Field(..., alias="Exercise angina", ge=0, le=1, example=0)
    st_depression: float = Field(..., alias="ST depression", ge=0.0, example=1.0)
    slope_of_st: int = Field(..., alias="Slope of ST", ge=0, le=2, example=2)
    number_of_vessels_fluro: int = Field(..., alias="Number of vessels fluro", ge=0, le=4, example=2)
    thallium: int = Field(..., alias="Thallium", ge=0, le=3, example=3)



class LiverDiseaseForm(BaseModel):
    Age: float = Field(..., gt=0, example=45)
    Gender: int = Field(...,ge=0, le=1, example=1,description="Male-1 Female-0")  
    Total_Bilirubin: float = Field(...,  gt=0, example=1.2)
    Direct_Bilirubin: float = Field(..., gt=0, example=0.4)
    Alkaline_Phosphotase: float = Field(..., gt=0, example=187.0)
    Alamine_Aminotransferase: float = Field(..., gt=0, example=16.0)
    Aspartate_Aminotransferase: float = Field(..., gt=0, example=54.0)
    Total_Protiens: float = Field(..., gt=0, example=6.8)
    Albumin: float = Field(..., gt=0, example=3.3)
    Albumin_and_Globulin_Ratio: float = Field(..., gt=0, example=0.9)

class DiabetesDisease(BaseModel):
    HighBP: Annotated[int, Field(ge=0, le=1, example=1)]
    HighChol: Annotated[int, Field(ge=0, le=1, example=1)]
    CholCheck: Annotated[int, Field(ge=0, le=1, example=1)]
    BMI: Annotated[float, Field(ge=0, le=100, example=28.7)]
    Smoker: Annotated[int, Field(ge=0, le=1, example=0)]
    Stroke: Annotated[int, Field(ge=0, le=1, example=0)]
    HeartDiseaseorAttack: Annotated[int, Field(ge=0, le=1, example=1)]
    PhysActivity: Annotated[int, Field(ge=0, le=1, example=1)]
    Fruits: Annotated[int, Field(ge=0, le=1, example=1)]
    Veggies: Annotated[int, Field(ge=0, le=1, example=1)]
    HvyAlcoholConsump: Annotated[int, Field(ge=0, le=1, example=0)]
    AnyHealthcare: Annotated[int, Field(ge=0, le=1, example=1)]
    NoDocbcCost: Annotated[int, Field(ge=0, le=1, example=0)]
    GenHlth: Annotated[int, Field(ge=1, le=5, example=3, description="1=Excellent, 5=Poor")]
    MentHlth: Annotated[int, Field(ge=0, le=30, example=5)]
    PhysHlth: Annotated[int, Field(ge=0, le=30, example=7)]
    DiffWalk: Annotated[int, Field(ge=0, le=1, example=1)]
    Sex: Annotated[int, Field(ge=0, le=1, example=1, description="Male=1, Female=0")]
    Age: Annotated[int, Field(ge=0, le=100, example=55)]
    Education: Annotated[int, Field(ge=1, le=6, example=5, description="1=Never, 6=College Graduate")]
    Income: Annotated[int, Field(ge=1, le=8, example=4, description="1=Lowest, 8=Highest")]
