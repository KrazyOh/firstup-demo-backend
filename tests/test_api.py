from copy import deepcopy

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def build_valid_payload() -> dict:
    return {
        "business_type": "Retail",
        "use_case": "safety",
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
                "image_key": "safety_frontline_operations_01",
            },
            {
                "name": "persona_1_city",
                "title": "Chicago Team News",
                "summary": "Updates for Chicago employees.",
                "body": "City-specific information for the Chicago team.",
                "image_key": "safety_frontline_chicago_01",
            },
            {
                "name": "persona_2_department",
                "title": "People Team Update",
                "summary": "News for the People department.",
                "body": "Department-specific information for HR leaders.",
                "image_key": "safety_corporate_people_01",
            },
            {
                "name": "persona_2_city",
                "title": "Dallas Office News",
                "summary": "Updates for Dallas employees.",
                "body": "City-specific information for the Dallas office.",
                "image_key": "safety_corporate_dallas_01",
            },
            {
                "name": "company_wide",
                "title": "Company Update",
                "summary": "News for everyone.",
                "body": (
                    "<h1>Safety Starts With Every Shift</h1>"
                    "<p>For frontline teams, this week introduces updated pre-shift "
                    "checklists and guest-area walkthrough expectations.</p>"
                    "<p>For corporate teams, leaders are launching a new safety "
                    "communications toolkit and reporting cadence.</p>"
                ),
                "image_key": "safety_companywide_01",
            },
        ],
    }


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_publish_demo_content_succeeds_with_valid_payload() -> None:
    payload = build_valid_payload()

    response = client.post("/publish-demo-content", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "received_payload": payload,
        "message": "Demo content received successfully",
    }


def test_publish_demo_content_fails_when_required_field_is_missing() -> None:
    payload = build_valid_payload()
    del payload["business_type"]

    response = client.post("/publish-demo-content", json=payload)

    assert response.status_code == 422


def test_publish_demo_content_fails_with_invalid_brand_color_hex() -> None:
    payload = build_valid_payload()
    payload["brand_colors"]["primary"] = "blue"

    response = client.post("/publish-demo-content", json=payload)

    assert response.status_code == 422
    assert "hex color" in str(response.json())


def test_publish_demo_content_fails_when_content_item_names_are_incomplete() -> None:
    payload = build_valid_payload()
    payload["content_items"] = payload["content_items"][:-1]

    response = client.post("/publish-demo-content", json=payload)

    assert response.status_code == 422
    assert "exactly these names" in str(response.json())


def test_publish_demo_content_fails_when_content_item_names_are_duplicated() -> None:
    payload = build_valid_payload()
    duplicated_payload = deepcopy(payload)
    duplicated_payload["content_items"][4]["name"] = "persona_1_department"

    response = client.post("/publish-demo-content", json=duplicated_payload)

    assert response.status_code == 422
    assert "duplicate names" in str(response.json())
