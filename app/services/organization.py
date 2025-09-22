from sqlalchemy import (
    select,
)
from sqlalchemy.orm import selectinload

from app.models.organization import (
    Organization,
)


async def get_organizations_by_building(building_id, session):
    """
    Returns all organization related to building.
    """
    query = select(Organization).options(
        selectinload(Organization.phones),
    ).where(
        Organization.building_id == building_id,
    )
    result = await session.execute(query)

    return result.scalars().unique().all()
