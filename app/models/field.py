from sqlalchemy import Nullable
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base
from models.organization import organization_field


class Field(Base):
    __tablename__ = "field"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(unique=False, index=False, nullable=True)
    name: Mapped[str] = mapped_column(unique=False, index=False)
    organizations = relationship("Organization", secondary=organization_field, back_populates="fields")
