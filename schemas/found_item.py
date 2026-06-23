from pydantic import BaseModel
from datetime import date


class FoundItemCreate(BaseModel):

    item_name: str

    category: str

    description: str

    found_date: date

    found_location: str

    image_url: str

    status: str = "Available"
