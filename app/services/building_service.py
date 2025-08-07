from typing import List, Optional

from sqlalchemy.orm import Session

from schemas.building import BuildingOutput, BuildingDetail

from repositories.building_repository import BuildingRepository


class BuildingService:

    def __init__(self, session: Session):

        self.repository = BuildingRepository(session)

    def get_by_id(self, _id: int) -> BuildingDetail:

        bld = self.repository.get_by_id(_id)

        return BuildingDetail(**bld.__dict__)


    def get_all(self) -> List[BuildingOutput]:

        return self.repository.get_all()
