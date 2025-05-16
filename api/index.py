import json
import requests
import os

RENDER_ENDPOINT = os.environ.get("RENDER_ENDPOINT")

def handler(request):
    try:
        if request.method != "POST":
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Method Not Allowed"})
            }

        data = request.get_json()

        if not RENDER_ENDPOINT:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "RENDER_ENDPOINT not set"})
            }

        res = requests.post(RENDER_ENDPOINT, json=data)
        return {
            "statusCode": res.status_code,
            "body": res.text
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
