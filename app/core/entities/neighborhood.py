from pydantic import BaseModel, Field
from app.core.utils import MyStr


class NeighborhoodInDB(BaseModel):

    id: int = Field(example=123)
    name: MyStr = Field(example="Viktor Konder")
