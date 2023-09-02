from pydantic import BaseModel, Field


class NeighborhoodInDB(BaseModel):

    id: int = Field(example=123)
    name: str = Field(example="Viktor Konder")
