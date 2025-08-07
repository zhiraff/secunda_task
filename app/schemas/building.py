from typing import Optional, List

from pydantic import BaseModel

from schemas.organization import OrganizationOutput


class BuildingOutput(BaseModel):
    id: int
    address: str


class BuildingDetail(BuildingOutput):
    lat: float
    lngt: float

class BuildingInPointWOrg(BuildingOutput):
    organization: Optional[List[OrganizationOutput]] = None
