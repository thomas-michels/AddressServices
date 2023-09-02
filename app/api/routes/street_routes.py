from fastapi import APIRouter, Depends
from .composers import address_composer
from app.core.services import AddressServices

router = APIRouter(prefix="/address", tags=["Address"])


@router.get("")
async def get_streets(services: AddressServices = Depends(address_composer)):
    ...
    # return await conn.execute("SELECT * FROM public.streets", many=True)
