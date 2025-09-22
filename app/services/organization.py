from sqlalchemy import (
    select,
)
from sqlalchemy.orm import (
    selectinload,
)

from app.models.activity import (
    Activity,
)
from app.models.organization import (
    Organization,
)


async def get_organizations_by_building(building_id: int, session):
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


async def get_organizations_by_activity(activity_id: int, session):
    """
    Returns all organizations associated with a certain activity.
    """
    query = select(Organization).join(
        Organization.activities,
    ).where(
        Activity.id == activity_id,
    ).options(
        selectinload(Organization.phones),
    )
    result = await session.execute(query)

    return result.scalars().all()
