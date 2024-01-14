from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials
from helpers.credentials_validation import verify_credentials
from models.content_generation_model import ContentGenerationRequest
from services.content_generation_service import content_generation_service, InvalidResponseException

generate_content_router = APIRouter()


@generate_content_router.post("/generate")
async def generate_content_endpoint(
    request: ContentGenerationRequest, credentials: HTTPBasicCredentials = Depends(verify_credentials)
) -> ContentGenerationRequest | dict:
    try:
        return await content_generation_service(request)
    except InvalidResponseException as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc))
    except HTTPException as http_exc:
        raise http_exc
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred")
