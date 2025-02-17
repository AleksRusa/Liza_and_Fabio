from pydantic import BaseModel

class Vote(BaseModel):
    option: str