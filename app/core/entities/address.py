from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    street: Optional[str] = Field(
        example="Rua Antonio da Veiga",
    )
    neighborhood: Optional[str] = Field(example="Viktor Konder")
    zip_code: Optional[str] = Field(example="89012-500", pattern=r"^\d{5}-\d{3}$")
    latitude: Optional[str] = Field(example="-26.8852955")
    longitude: Optional[str] = Field(example="-49.0808952")
    flood_quota: Optional[float] = Field(example=10.5)


class PlainAddress(BaseModel):
    street_name: Optional[str] = Field(
        example="Rua Antonio da Veiga",
    )
    street_id: int = Field(example=123)
    neighborhood_name: Optional[str] = Field(example="Viktor Konder")
    neighborhood_id: int = Field(example=123)
    # zip_code: Optional[str] = Field(example="89012-500", pattern=r"^\d{5}-\d{3}$")
    zip_code: Optional[str] = Field(example="89012-500")
    latitude: Optional[str] = Field(example="-26.8852955")
    longitude: Optional[str] = Field(example="-49.0808952")
    flood_quota: Optional[float] = Field(example=10.5)
