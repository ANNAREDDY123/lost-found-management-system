from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(
        Integer,
        primary_key=True
    )

    found_item_id = Column(
        Integer,
        ForeignKey("found_items.id")
    )

    user_id = Column(Integer)

    status = Column(
        String,
        default="Pending"
    )
