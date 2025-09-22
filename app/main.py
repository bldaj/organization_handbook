from fastapi import (
    FastAPI,
)

from app.api import (
    organization,
)


app = FastAPI()

app.include_router(organization.router)


@app.get('/')
async def root():
    return {'status': 'ok'}
