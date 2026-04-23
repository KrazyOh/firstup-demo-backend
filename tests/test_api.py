from copy import deepcopy

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def build_valid_payload() -> dict:
    return {
        "business_type": "Retail",
        "use_case": "safety_compliance",
        "personas": {
            "persona_1": {
                "persona_type": "frontline",
                "job_title": "Store Associate",
                "department": "Operations",
                "city": "Chicago",
            },
            "persona_2": {
                "persona_type": "corporate",
                "job_title": "HR Manager",
                "department": "People",
                "city": "Dallas",
            },
        },
        "brand_colors": {
            "primary": "#003366",
            "secondary": "#00A3E0",
            "accent": "#FFB81C",
        },
        "content_items": [
            {
                "name": "persona_1_department",
                "title": "Operations Update",
                "summary": "Quick update for operations teams.",
                "body": "Important operational guidance for store teams.",
                "image_key": "safety_compliance_frontline_department_01",
            },
            {
                "name": "persona_1_city",
                "title": "Chicago Team News",
                "summary": "Updates for Chicago employees.",
                "body": "City-specific information for the Chicago team.",
                "image_key": "safety_compliance_frontline_city_01",
            },
            {
                "name": "persona_2_department",
                "title
