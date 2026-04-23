from fastapi import FastAPI

from app.config import load_firstup_settings
from app.models import PublishDemoContentRequest, PublishDemoContentResponse
from app.publish_service import DemoPublishService


app = FastAPI(
    title="Firstup Demo Backend",
    version="0.1.0",
    description="Backend scaffold for a Firstup demo workflow.",
)


@app.get("/health")
async def health_check() -> dict[str, bool]:
    return {"ok": True}


@app.post("/publish-demo-content", response_model=PublishDemoContentResponse)
async def publish_demo_content(
    payload: PublishDemoContentRequest,
) -> PublishDemoContentResponse:
    settings = load_firstup_settings()
    publish_service = DemoPublishService(settings)
    publish_service.prepare_demo_content(payload)

    return PublishDemoContentResponse(
        success=True,
        received_payload=payload,
        message="Demo content received successfully",
    )
