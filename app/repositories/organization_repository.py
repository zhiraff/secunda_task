from typing import List, Optional, Type

from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session, joinedload

from models.building import Building
from models.field import Field
from models.organization import Organization
from schemas.building import BuildingInPointWOrg
from schemas.organization import OrganizationOutput, OrganizationDetail


class OrganizationRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Optional[OrganizationOutput]]:
        orgs = self.session.query(Organization).all()
        return self._map_to_schema_list(orgs)

    @staticmethod
    def _map_to_schema_list(orgs: List[Type[Organization]]) -> List[OrganizationOutput]:
        return [
            OrganizationOutput(
                id=org.id,
                name=org.name,
                number=org.number,
                building=org.building_id,
                fields=org.fields,
            )
            for org in orgs
        ]
    #
    def get_by_id(self, _id: int) -> Type[Organization]:
        org = self.session.query(Organization).filter_by(id=_id).first()
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
        return org

    def get_by_building_id(self, _id: int) -> List[OrganizationOutput]:
        orgs = self.session.query(Organization).filter_by(building_id=_id).all()
        return self._map_to_schema_list(orgs)

    def get_by_field_id(self, _id: int) -> List[OrganizationOutput]:
        fld = self.session.query(Field).filter(Field.id == _id).first()

        if not fld:
            raise HTTPException(status_code=404, detail="Field not found")
        orgs = fld.organizations
        return self._map_to_schema_list(orgs)

    def get_by_name(self, _value: str) -> List[OrganizationOutput]:
        orgs = self.session.query(Organization).filter(Organization.name.ilike(f"%{_value}%")).all()
        return self._map_to_schema_list(orgs)

    def get_by_point(self, _lat: float, _lngt: float, _radius: float) -> List[BuildingInPointWOrg]:
        if _lat < 0 and _lngt < 0:
            blds = self.session.query(Building).filter(Building.lat < 0, Building.lngt < 0).all()
        elif _lat < 0 and _lngt > 0:
            blds = self.session.query(Building).filter(Building.lat < 0, Building.lngt > 0).all()
        elif _lat > 0 and _lngt < 0:
            blds = self.session.query(Building).filter(Building.lat > 0, Building.lngt < 0).all()
        else:
            blds = self.session.query(Building).filter(Building.lat > 0, Building.lngt > 0).all()
        res = []
        for bld in blds:
            kat1 = bld.lat - _lat
            kat2 = bld.lngt - _lngt
            if (kat1**2 + kat2**2)**0.5 <= _radius:
                orgs = self.session.query(Organization).filter(Organization.building_id==bld.id).all()
                res.append(
                    BuildingInPointWOrg(
                        id=bld.id,
                        address=bld.address,
                        organization=[OrganizationOutput(id=org.id, name=org.name) for org in orgs]
                    )
                )
        return res


    def get_by_field_including_id(self, _id: int) -> List[OrganizationOutput]:
        fields = self.session.query(Field.id).filter((Field.id == _id) | (Field.parent_id == _id)).all()
        ids = [field[0] for field in fields]
        orgs = self.session.query(Organization).join(Organization.fields).filter(Field.id.in_(ids)).all()
        return self._map_to_schema_list(orgs)
