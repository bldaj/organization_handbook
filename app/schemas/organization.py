from pydantic import (
    BaseModel,
)


class OrganizationBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class OrganizationWithPhones(OrganizationBase):
    phones: list[str] = []
