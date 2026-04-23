from typing import List, Literal
import re

from pydantic import BaseModel, Field, field_validator, model_validator

from app.image_keys import ALLOWED_IMAGE_KEYS


HEX_COLOR_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")


class Persona(BaseModel):
    persona_type: Literal["frontline", "corporate"]
    job_title: str = Field(..., min_length=1)
    department: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)


class BrandColors(BaseModel):
    primary: str = Field(..., min_length=1)
    secondary: str = Field(..., min_length=1)
    accent: str = Field(..., min_length=1)

    @field_validator("primary", "secondary", "accent")
    @classmethod
    def validate_hex_color(cls, value: str) -> str:
        if not HEX_COLOR_PATTERN.fullmatch(value):
            raise ValueError("must be a valid hex color in the format #RRGGBB")
        return value


class ContentItem(BaseModel):
    name: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    summary: str = Field(..., min_length=1)
    body: str = Field(..., min_length=1)
    image_key: str = Field(..., min_length=1)

    @field_validator("image_key")
    @classmethod
    def validate_image_key(cls, value: str) -> str:
        if value not in ALLOWED_IMAGE_KEYS:
            raise ValueError("must be an approved image_key from the image library")
        return value


class Personas(BaseModel):
    persona_1: Persona
    persona_2: Persona


class PublishDemoContentRequest(BaseModel):
    business_type: str = Field(..., min_length=1)
    use_case: str = Field(..., min_length=1)
    personas: Personas
    brand_colors: BrandColors
    content_items: List[ContentItem] = Field(..., min_length=1)

    @model_validator(mode="after")
    def validate_content_items(self) -> "PublishDemoContentRequest":
        expected_names = {
            "persona_1_department",
            "persona_1_city",
            "persona_2_department",
            "persona_2_city",
            "company_wide",
        }
        actual_names_list = [item.name for item in self.content_items]

        if len(actual_names_list) != len(set(actual_names_list)):
            raise ValueError("content_items must not contain duplicate names")

        actual_names = set(actual_names_list)

        if actual_names != expected_names:
            raise ValueError(
                "content_items must include exactly these names: "
                "persona_1_department, persona_1_city, persona_2_department, "
                "persona_2_city, company_wide"
            )

        return self


class PublishDemoContentResponse(BaseModel):
    success: bool = True
    received_payload: PublishDemoContentRequest
    message: str


class FirstupAuthCheckResponse(BaseModel):
    ok: bool
    configured: bool
    message: str
