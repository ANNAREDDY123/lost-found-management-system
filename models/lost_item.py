from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)

from database import Base


class LostItem(Base):
    __tablename__ = "lost_items"

    id = Column(
        Integer,
        primary_key=True
    )

    item_name = Column(String)

    category = Column(String)

    description = Column(String)

    lost_date = Column(Date)

    lost_location = Column(String)

    image_url = Column(String)

    status = Column(
        String,
        default="Open"
    )
