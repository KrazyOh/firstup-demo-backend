# Firstup Demo FastAPI Backend

Small FastAPI backend scaffold for a Firstup demo workflow. This version validates the request payload and echoes the validated data back. It does not publish to Firstup yet.

## Requirements

- Python 3.11+

## Install dependencies

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Keep secrets in environment variables only.

Example:

```bash
export FIRSTUP_API_KEY="your-secret-here"
```

## Run the app locally

```bash
python --version
uvicorn app.main:app --reload
```

You should see Python 3.11 or newer after activating the virtual environment.

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /health`
- `POST /publish-demo-content`

## Example curl request

```bash
curl -X POST "http://127.0.0.1:8000/publish-demo-content" \
  -H "Content-Type: application/json" \
  -d '{
    "business_type": "Retail",
    "personas": {
      "persona_1": {
        "persona_type": "frontline",
        "job_title": "Store Associate",
        "department": "Operations",
        "city": "Chicago"
      },
      "persona_2": {
        "persona_type": "corporate",
        "job_title": "HR Manager",
        "department": "People",
        "city": "Dallas"
      }
    },
    "brand_colors": {
      "primary": "#003366",
      "secondary": "#00A3E0",
      "accent": "#FFB81C"
    },
    "content_items": [
      {
        "name": "persona_1_department",
        "title": "Operations Update",
        "summary": "Quick update for operations teams.",
        "body": "Important operational guidance for store teams."
      },
      {
        "name": "persona_1_city",
        "title": "Chicago Team News",
        "summary": "Updates for Chicago employees.",
        "body": "City-specific information for the Chicago team."
      },
      {
        "name": "persona_2_department",
        "title": "People Team Update",
        "summary": "News for the People department.",
        "body": "Department-specific information for HR leaders."
      },
      {
        "name": "persona_2_city",
        "title": "Dallas Office News",
        "summary": "Updates for Dallas employees.",
        "body": "City-specific information for the Dallas office."
      },
      {
        "name": "company_wide",
        "title": "Company Update",
        "summary": "News for everyone.",
        "body": "A company-wide message for all employees."
      }
    ]
  }'
```

## Response shape

Successful `POST /publish-demo-content` responses return:

```json
{
  "success": true,
  "received_payload": {},
  "message": "Demo content payload received successfully."
}
```

