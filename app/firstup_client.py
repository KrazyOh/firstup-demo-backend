from app.config import FirstupSettings


class FirstupClient:
    def __init__(self, settings: FirstupSettings) -> None:
        self.settings = settings

    def is_configured(self) -> bool:
        return all(
            [
                self.settings.region,
                self.settings.client_id,
                self.settings.client_secret,
                self.settings.auth_url,
                self.settings.api_base_url,
            ]
        )

    def publish_content(self) -> None:
        # Real Firstup publishing will be added in a later phase.
        raise NotImplementedError("Firstup publishing is not implemented yet")
