from functools import (
    lru_cache,
)
from typing import (
    Annotated,
)

from fastapi import (
    Depends,
)
from sqlalchemy.ext.asyncio.session import (
    AsyncSession,
)

from app.core.config import (
    Settings,
)
from app.db.session import (
    get_session,
)


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]

SessionDep = Annotated[AsyncSession, Depends(get_session)]
