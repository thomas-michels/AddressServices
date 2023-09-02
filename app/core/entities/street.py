from typing import Optional
from pydantic import BaseModel, Field

class Street(BaseModel):
    name: str = Field(example="Antonio da Veiga")
    neighborhood_id: int = Field(example=123)
    # zip_code: Optional[str] = Field(default=None, example="89012-500", pattern=r'^\d{5}-\d{3}$')
    zip_code: Optional[str] = Field(default=None, example="89012-500")
    latitude: Optional[str] = Field(default=None, example="-26.8852955")
    longitude: Optional[str] = Field(default=None, example="-49.0808952")
    flood_quota: Optional[float] = Field(default=None, example=10.5)


class StreetInDB(Street):
    id: int = Field(example=123)
