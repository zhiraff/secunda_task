from typing import List, Optional

from sqlalchemy.orm import Session

from schemas.field import FieldOutput, FieldDetail

from repositories.field_repository import FieldRepository


class FieldService:

    def __init__(self, session: Session):

        self.repository = FieldRepository(session)

    def get_by_id(self, _id: int) -> FieldDetail:

        fld = self.repository.get_by_id(_id)

        return FieldDetail(**fld.__dict__)


    def get_all(self) -> List[FieldOutput]:

        return self.repository.get_all()
