from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.building import BuildingInPointWOrg
from services.organization_service import OrganizationService
from schemas.organization import OrganizationOutput, OrganizationDetail
from config.database import get_db


router = APIRouter(
    prefix="/org",
    tags=["Организации"]
)


@router.get("/", status_code=200, response_model=List[OrganizationOutput])
def get_org(session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех организаций.

    Аргументы:

    Returns:
        List[OrganizationOutput]: Список органов.
    """

    _service = OrganizationService(session)
    return _service.get_all()

@router.get("/{_id}", status_code=200, response_model=OrganizationDetail)
def get_org_by_id(_id: int, session: Session = Depends(get_db),
                   # current_user: UserKeycloak = Depends(get_current_user)
                   ):

    _service = OrganizationService(session)
    res = _service.get_by_id(_id)
    if not res:
        raise HTTPException(status_code=404, detail="Org not found")
    return res

@router.get("/by_building_id/{_id}", status_code=200, response_model=List[OrganizationOutput])
def get_by_building_id(_id: int, session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех организаций в конкретном здании.

    Args:
        _id (int): ID of the building.
    Returns:
        List[OrganizationOutput]: Список орг.
    """

    _service = OrganizationService(session)
    return _service.get_by_building_id(_id)

@router.get("/by_field_id/{_id}", status_code=200, response_model=List[OrganizationOutput])
def get_by_field_id(_id: int, session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех организаций по кокретной деятельности.

    Args:
        _id (int): ID of the field.
    Returns:
        List[OrganizationOutput]: Список орг.
    """

    _service = OrganizationService(session)
    return _service.get_by_field_id(_id)

@router.get("/search_name/{_value}", status_code=200, response_model=List[OrganizationOutput])
def get_by_name(_value: str, session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех организаций по кокретной деятельности.

    Args:
        _value (str): что искать.
    Returns:
        List[OrganizationOutput]: Список орг.
    """

    _service = OrganizationService(session)
    return _service.get_by_name(_value)


@router.post("/by_point/", status_code=200, response_model=List[BuildingInPointWOrg])
def get_by_point(_lat: float, _lngt: float, _radius: float, session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех зданий с организациями в радиусе от конкретной точки.

    Args:
        _lat (float): Широта.
        _lngt (float): Долгота
        _radius (float): Радиус
    Returns:
        List[OrganizationOutput]: Список орг.
    """

    _service = OrganizationService(session)
    return _service.get_by_point(_lat, _lngt, _radius)

@router.get("/by_field_id_including/{_id}", status_code=200, response_model=List[OrganizationOutput])
def get_by_field_including_id(_id: int, session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список всех организаций по деятельности в глубину.

    Args:
        _id (int): ID деятельности.
    Returns:
        List[OrganizationOutput]: Список орг.
    """

    _service = OrganizationService(session)
    return _service.get_by_field_including_id(_id)