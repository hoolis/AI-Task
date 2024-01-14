from fastapi import FastAPI
from endpoints.rephraser_endpoint import rephraser_router
from endpoints.content_generation_endpoint import generate_content_router

app = FastAPI()

app.include_router(rephraser_router, prefix="/api", tags=["Rephraser"])
app.include_router(generate_content_router, prefix="/api", tags=["Content Generation"])
