from pydantic import BaseModel, Field, Extra


class RephraseRequest(BaseModel):
    text: str = Field(..., description="Text to be rephrased")
    number_of_variants: int = Field(ge=1, description="Number of variants, must be at least 1")

    class Config:
        extra = Extra.forbid
