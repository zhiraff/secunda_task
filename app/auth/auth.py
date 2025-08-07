from fastapi import HTTPException, Header, Depends
from fastapi.security import APIKeyHeader

from config.settings import settings

api_key_scheme = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_scheme)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
