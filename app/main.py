import os

from fastapi import FastAPI

from app.models import PublishDemoContentRequest, PublishDemoContentResponse


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
    # Placeholder for future env-based integration settings.
    _ = os.getenv("FIRSTUP_API_KEY")

    return PublishDemoContentResponse(
        success=True,
        received_payload=payload,
        message="Demo content received successfully",
    )
