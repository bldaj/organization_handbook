from fastapi import (
    Depends,
)
from fastapi.routing import (
    APIRouter,
)

from app.core.security import (
    verify_api_key,
)
from app.dependencies import (
    SessionDep,
)
from app.schemas.organization import (
    OrganizationWithPhones,
)
from app.services.organization import (
    get_organizations_by_activity,
    get_organizations_by_building,
)


router = APIRouter(
    prefix='/organizations',
    dependencies=[Depends(verify_api_key)],
    tags=['Organizations'],
)


@router.get('/by-building', response_model=list[OrganizationWithPhones])
async def organization_list_by_building(building_id: int, session: SessionDep):
    """
    Endpoint to get all organizations located in the specified building.
    """
    organizations = await get_organizations_by_building(building_id, session)

    return [
        {
            "id": org.id,
            "name": org.name,
            "phones": [phone.phone for phone in org.phones],
        }
        for org in organizations
    ]


@router.get('/by-activity', response_model=list[OrganizationWithPhones])
async def organization_list_by_activity(activity_id: int, session: SessionDep):
    """
    Endpoint to get all organizations associated with a certain activity.
    """
    organizations = await get_organizations_by_activity(activity_id, session)

    return [
        {
            "id": org.id,
            "name": org.name,
            "phones": [phone.phone for phone in org.phones],
        }
        for org in organizations
    ]
