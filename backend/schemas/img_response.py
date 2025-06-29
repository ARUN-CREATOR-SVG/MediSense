from pydantic import BaseModel
from typing import Literal

class PneumoniaPredictionResponse(BaseModel):
    prediction: Literal["NORMAL", "PNEUMONIA"]
    confidence: float  
