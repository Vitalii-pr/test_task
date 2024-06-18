from pydantic import BaseModel, Field

class TextToSummarizer(BaseModel):
    text: str

class SummarizedText(BaseModel):
    summarized: str = Field(validation_alias='text')