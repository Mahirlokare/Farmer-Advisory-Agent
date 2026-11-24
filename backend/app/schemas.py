from pydantic import BaseModel, Field
from typing import Literal

Language = Literal["en", "hi", "mr", "gu", "ta", "te"]
MessageRole = Literal["user", "assistant"]

class ConversationMessage(BaseModel):
    role: MessageRole
    content: str = Field(min_length=1, max_length=4000)

class AdvisoryRequest(BaseModel):
    language: Language = "en"
    crop: str = Field(min_length=2, max_length=80)
    location: str = Field(min_length=2, max_length=120)
    soil_type: str | None = Field(default=None, max_length=80)
    question: str = Field(min_length=5, max_length=2000)
    conversation_history: list[ConversationMessage] = Field(default_factory=list, max_length=12)

class WeatherRequest(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

class DiseaseTriageResponse(BaseModel):
    status: str
    message: str
    model_ready: bool = False
