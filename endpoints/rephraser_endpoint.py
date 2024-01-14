from typing import List
from fastapi.security import HTTPBasicCredentials
from helpers.credentials_validation import verify_credentials
from services.rephraser_service import rephraser_service, InvalidResponseException
from fastapi import APIRouter, HTTPException, status, Depends
from models.rephraser_model import RephraseRequest

rephraser_router = APIRouter()


@rephraser_router.post("/rephrase")
async def rephrase_endpoint(
    request: RephraseRequest, credentials: HTTPBasicCredentials = Depends(verify_credentials)
) -> List | dict:
    try:
        return await rephraser_service(request)
    except InvalidResponseException as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc))
    except HTTPException as http_exc:
        raise http_exc
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred")
