from typing import List, Optional, Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.building import Building
from schemas.building import BuildingOutput, BuildingDetail


class BuildingRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Optional[BuildingOutput]]:
        blds = self.session.query(Building).all()
        return self._map_to_schema_list(blds)

    @staticmethod
    def _map_to_schema_list(blds: List[Type[Building]]) -> List[BuildingOutput]:
        return [
            BuildingOutput(
                id=bld.id,
                address=bld.address,
            )
            for bld in blds
        ]
    #
    def get_by_id(self, _id: int) -> Type[Building]:
        bld = self.session.query(Building).filter_by(id=_id).first()
        if not bld:
            raise HTTPException(status_code=404, detail="Building not found")
        return bld
