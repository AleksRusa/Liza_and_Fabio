from pydantic import BaseModel
# from sqlalchemy.orm import Base

# from database import Base




class Vote(BaseModel):
    option: str