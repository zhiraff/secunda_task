from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.auth import validate_api_key
from services.building_service import BuildingService
from schemas.building import BuildingOutput, BuildingDetail
from config.database import get_db


router = APIRouter(
    prefix="/building",
    tags=["Здания"]
)


@router.get("/{_id}", status_code=200, response_model=BuildingDetail)
def get_by_id(_id: int, session: Session = Depends(get_db),
              ):
    """
    Показать детально одно здание

    Args:
        _id (int): ID of the building.
        session (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        BuildingDetail: building.
    """
    _service = BuildingService(session)
    res = _service.get_by_id(_id)
    if not res:
        raise HTTPException(status_code=404, detail="Building not found")
    return res


@router.get("/", status_code=200, response_model=List[BuildingOutput])
def get_building(session: Session = Depends(get_db),
                 ):
    """
    Получить список зданий.

    Аргументы:

    Returns:
        List[BuildingOutput]: Список зданий.
    """

    _service = BuildingService(session)
    return _service.get_all()
