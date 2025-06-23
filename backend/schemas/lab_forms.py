from pydantic import BaseModel,Field

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

