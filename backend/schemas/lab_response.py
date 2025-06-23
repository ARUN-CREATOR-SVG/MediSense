from pydantic import BaseModel,Field

class HeartDiseaseResponse(BaseModel):
    risk_level:float
    prediction:int
    probability:float

class LiverDiseaseResponse(HeartDiseaseResponse):
    pass