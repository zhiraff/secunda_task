from typing import Optional, List

from pydantic import BaseModel


class FieldOutput(BaseModel):
    id: int
    parent_id: Optional[int] = None
    name: str


class FieldDetail(FieldOutput):
    organizations: Optional[List[str]] = None
