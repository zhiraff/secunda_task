from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from config.database import Base


class Building(Base):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=False, index=False)
    lat: Mapped[float] = mapped_column(Float(precision=15, decimal_return_scale=8), unique=False, index=False, nullable=True)
    lngt: Mapped[float] = mapped_column(Float(precision=15, decimal_return_scale=8), unique=False, index=False, nullable=True)
    organization = relationship("Organization", back_populates="building")

    @validates('lat', 'lngt')
    def validate_coords(self, key: str, value: float) -> float:
        if key == 'lat' and not (-90 <= value <= 90):
            raise ValueError("Широта должна быть между -90 и 90")
        if key == 'lngt' and not (-180 <= value <= 180):
            raise ValueError("Долгота должна быть между -180 и 180")
        return value
