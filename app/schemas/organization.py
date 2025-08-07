from typing import Optional, List

from pydantic import BaseModel


class OrganizationOutput(BaseModel):
    id: int
    name: str


class OrganizationDetail(OrganizationOutput):
    number: str
    building_id: int
    fields: Optional[List[str]] = None
