# Firstup Demo FastAPI Backend

Small FastAPI backend scaffold for a Firstup demo workflow. This version validates the request payload and echoes the validated data back. It does not publish to Firstup yet.

## Requirements

- Python 3.11+

## Install dependencies

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Environment variables
Keep secrets in environment variables only.

Example:

export FIRSTUP_REGION="US1"
export FIRSTUP_CLIENT_ID="your-client-id"
export FIRSTUP_CLIENT_SECRET="your-client-secret"
export FIRSTUP_AUTH_URL="https://auth.socialchorus.com/oauth/token"
export FIRSTUP_API_BASE_URL="https://partner.socialchorus.com"
export FIRSTUP_ENABLE_PUBLISHING="false"
Publishing remains disabled in this scaffold until the real Firstup integration is added.

Run the app locally
python --version
uvicorn app.main:app --reload
You should see Python 3.11 or newer after activating the virtual environment.

The API will be available at http://127.0.0.1:8000.

Endpoints
GET /health
POST /publish-demo-content
Example curl request
curl -X POST "http://127.0.0.1:8000/publish-demo-content" \
  -H "Content-Type: application/json" \
  -d '{
    "business_type": "Retail",
    "use_case": "safety_compliance",
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
        "body": "Important operational guidance for store teams.",
        "image_key": "safety_compliance_frontline_department_01"
      },
      {
        "name": "persona_1_city",
        "title": "Chicago Team News",
        "summary": "Updates for Chicago employees.",
        "body": "City-specific information for the Chicago team.",
        "image_key": "safety_compliance_frontline_city_01"
      },
      {
        "name": "persona_2_department",
        "title": "People Team Update",
        "summary": "News for the People department.",
        "body": "Department-specific information for HR leaders.",
        "image_key": "safety_compliance_corporate_department_01"
      },
      {
        "name": "persona_2_city",
        "title": "Dallas Office News",
        "summary": "Updates for Dallas employees.",
        "body": "City-specific information for the Dallas office.",
        "image_key": "safety_compliance_corporate_city_01"
      },
      {
        "name": "company_wide",
        "title": "Safety Starts With Every Shift",
        "summary": "A company-wide safety update tailored to frontline and corporate teams.",
        "body": "<h1>Safety Starts With Every Shift</h1><p>For frontline teams, this week introduces updated pre-shift checklists and guest-area walkthrough expectations.</p><p>For corporate teams, leaders are launching a new safety communications toolkit and reporting cadence.</p>",
        "image_key": "safety_compliance_companywide_01"
      }
    ]
  }'
Response shape
Successful POST /publish-demo-content responses return:

{
  "success": true,
  "received_payload": {},
  "message": "Demo content received successfully"
}
