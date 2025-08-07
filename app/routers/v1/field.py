from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from services.field_service import FieldService
from schemas.field import FieldOutput, FieldDetail
from config.database import get_db


router = APIRouter(
    prefix="/field",
    tags=["Сферы деятельности"]
)


@router.get("/{_id}", status_code=200, response_model=FieldDetail)
def get_by_id(_id: int, session: Session = Depends(get_db),
                   # current_user: UserKeycloak = Depends(get_current_user)
              ):
    """
    Показать детально одну сферу

    Args:
        _id (int): ID of the field.
        session (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        FieldDetail: field.
    """
    _service = FieldService(session)
    res = _service.get_by_id(_id)
    if not res:
        raise HTTPException(status_code=404, detail="Field not found")
    return res


@router.get("/", status_code=200, response_model=List[FieldOutput])
def get_building(session: Session = Depends(get_db)):
# def get_building(current_user: UserKeycloak = Depends(get_current_user),
#              session: Session = Depends(get_db)):
    """
    Получить список сфер.

    Аргументы:

    Returns:
        List[FieldOutput]: Список сфер.
    """

    _service = FieldService(session)
    return _service.get_all()
