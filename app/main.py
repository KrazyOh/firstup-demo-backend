from fastapi import FastAPI

from app.config import load_firstup_settings
from app.models import (
    FirstupAuthCheckResponse,
    PublishDemoContentRequest,
    PublishDemoContentResponse,
)
from app.publish_service import DemoPublishService


app = FastAPI(
    title="Firstup Demo Backend",
    version="0.1.0",
    description="Backend scaffold for a Firstup demo workflow.",
)


@app.get("/health")
async def health_check() -> dict[str, bool]:
    return {"ok": True}


@app.get("/firstup-auth-check", response_model=FirstupAuthCheckResponse)
async def firstup_auth_check() -> FirstupAuthCheckResponse:
    settings = load_firstup_settings()
    publish_service = DemoPublishService(settings)

    if not publish_service.firstup_client.is_configured():
        return FirstupAuthCheckResponse
