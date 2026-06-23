from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)

from database import Base


class FoundItem(Base):
    __tablename__ = "found_items"

    id = Column(
        Integer,
        primary_key=True
    )

    item_name = Column(String)

    category = Column(String)

    description = Column(String)

    found_date = Column(Date)

    found_location = Column(String)

    image_url = Column(String)

    status = Column(
        String,
        default="Available"
    )
