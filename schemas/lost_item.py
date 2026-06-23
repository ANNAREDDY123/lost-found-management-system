from pydantic import BaseModel
from datetime import date


class LostItemCreate(BaseModel):

    item_name: str

    category: str

    description: str

    lost_date: date

    lost_location: str

    image_url: str

    status: str = "Open"
