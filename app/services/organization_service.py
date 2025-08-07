from typing import List, Optional

from sqlalchemy.orm import Session

from schemas.building import BuildingInPointWOrg
from schemas.organization import OrganizationOutput, OrganizationDetail

from repositories.organization_repository import OrganizationRepository


class OrganizationService:

    def __init__(self, session: Session):

        self.repository = OrganizationRepository(session)

    def get_by_id(self, _id: int) -> OrganizationDetail:

        org = self.repository.get_by_id(_id)
        org_dict = {k: v for k, v in org.__dict__.items() if not k.startswith('_')}

        return OrganizationDetail(**org_dict)

    def get_all(self) -> List[OrganizationOutput]:

        return self.repository.get_all()

    def get_by_building_id(self, _id: int) -> List[OrganizationOutput]:

        return self.repository.get_by_building_id(_id)

    def get_by_field_id(self, _id) -> List[OrganizationOutput]:

        return self.repository.get_by_field_id(_id)

    def get_by_name(self, _value) -> List[OrganizationOutput]:

        return self.repository.get_by_name(_value)

    def get_by_point(self, _lat: float, _lngt: float, _radius: float) ->  List[BuildingInPointWOrg]:

        return self.repository.get_by_point(_lat, _lngt, _radius)

    def get_by_field_including_id(self, _id: int) ->  List[OrganizationOutput]:

        return self.repository.get_by_field_including_id(_id)
