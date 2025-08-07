from typing import List, Optional, Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.field import Field
from schemas.field import FieldOutput, FieldDetail


class FieldRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Optional[FieldOutput]]:
        flds = self.session.query(Field).all()
        return self._map_to_schema_list(flds)

    @staticmethod
    def _map_to_schema_list(flds: List[Type[Field]]) -> List[FieldOutput]:
        return [
            FieldOutput(
                id=fld.id,
                parent_id=fld.parent_id,
                name=fld.name,
            )
            for fld in flds
        ]
    #
    def get_by_id(self, _id: int) -> Type[Field]:
        fld = self.session.query(Field).filter_by(id=_id).first()
        if not fld:
            raise HTTPException(status_code=404, detail="Field not found")
        return fld
