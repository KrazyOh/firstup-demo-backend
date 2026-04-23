from app.config import FirstupSettings
from app.firstup_client import FirstupClient
from app.models import PublishDemoContentRequest


class DemoPublishService:
    def __init__(self, settings: FirstupSettings) -> None:
        self.settings = settings
        self.firstup_client = FirstupClient(settings)

    def can_authenticate_to_firstup(self) -> bool:
        if not self.firstup_client.is_configured():
            return False

        return self.firstup_client.check_authentication()

    def prepare_demo_content(self, payload: PublishDemoContentRequest) -> None:
        # Keep the first version side-effect free while still validating that
        # the future Firstup integration settings can be loaded safely.
        if self.settings.enable_publishing and self.firstup_client.is_configured():
            self.firstup_client.publish_content()

        _ = payload
