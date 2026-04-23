import os
from dataclasses import dataclass


@dataclass(frozen=True)
class FirstupSettings:
    region: str = ""
    client_id: str = ""
    client_secret: str = ""
    auth_url: str = ""
    api_base_url: str = ""
    enable_publishing: bool = False


def load_firstup_settings() -> FirstupSettings:
    return FirstupSettings(
        region=os.getenv("FIRSTUP_REGION", ""),
        client_id=os.getenv("FIRSTUP_CLIENT_ID", ""),
        client_secret=os.getenv("FIRSTUP_CLIENT_SECRET", ""),
        auth_url=os.getenv("FIRSTUP_AUTH_URL", ""),
        api_base_url=os.getenv("FIRSTUP_API_BASE_URL", ""),
        enable_publishing=os.getenv("FIRSTUP_ENABLE_PUBLISHING", "false").lower()
        == "true",
    )
