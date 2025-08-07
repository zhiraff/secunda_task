from sqlalchemy import ForeignKey, Column, Table, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


organization_field = Table(
    'organization_field',
    Base.metadata,
    Column('organuzation_id', Integer, ForeignKey('organization.id')),
    Column('field_id', Integer, ForeignKey('field.id'))
)


class Organization(Base):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=False, index=False)
    number: Mapped[str] = mapped_column(unique=False, index=False)
    building_id: Mapped[int] = mapped_column(ForeignKey("building.id", ondelete='RESTRICT'))
    building: Mapped['Building'] = relationship(back_populates='organization')
    fields = relationship("Field", secondary=organization_field, back_populates="organizations")
