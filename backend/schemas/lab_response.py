from pydantic import BaseModel

class HeartDiseaseResponse(BaseModel):
    risk_level:str
    prediction:int
    probability:float

class LiverDiseaseResponse(HeartDiseaseResponse):
    pass

class DiabetesDiseaseResponse(HeartDiseaseResponse):
    pass