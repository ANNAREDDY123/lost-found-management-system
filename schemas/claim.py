from pydantic import BaseModel


class ClaimCreate(BaseModel):

    user_id: int


class ClaimUpdate(BaseModel):

    status: str
