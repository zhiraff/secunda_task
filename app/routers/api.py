from fastapi import APIRouter, Depends

from auth.auth import validate_api_key
from routers.v1 import building, field, organization

router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(validate_api_key)]
)

router.include_router(building.router)
router.include_router(field.router)
router.include_router(organization.router)

