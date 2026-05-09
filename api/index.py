from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Apna JWT yaha daalo
JWT = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxMjk3Njk5MjU5NCwibmlja25hbWUiOiJmQ0lZZEhCekprNVQiLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiI0NTU4Y2FhMjcyZWM5ZTRiNWQ3Y2ZhMThkMjY1ZjkyZCIsImV4dGVybmFsX3R5cGUiOjQsInBsYXRfaWQiOjEsImNsaWVudF92ZXJzaW9uIjoiMS4xMDguMyIsImVtdWxhdG9yX3Njb3JlIjoxMDAsImlzX2VtdWxhdG9yIjp0cnVlLCJjb3VudHJ5X2NvZGUiOiJVUyIsImV4dGVybmFsX3VpZCI6NDEwMzY3MjUwOCwicmVnX2F2YXRhciI6MTAyMDAwMDA3LCJzb3VyY2UiOjAsImxvY2tfcmVnaW9uX3RpbWUiOjE3NTUwMTkwNzAsImNsaWVudF90eXBlIjoyLCJzaWduYXR1cmVfbWQ1IjoiIiwidXNpbmdfdmVyc2lvbiI6MCwicmVsZWFzZV9jaGFubmVsIjoiIiwicmVsZWFzZV92ZXJzaW9uIjoiT0I1MyIsImV4cCI6MTc3ODI4NDA5NH0.x7pOlOSlXhdtWDqtSi5hcT7agwenb0mqz34T3_qT1t0"

@app.route("/user-details")
def user_details():
    user_id = request.args.get("user")

    if not user_id:
        return jsonify({"success": False, "error": "Missing user ID"}), 400

    url = f"https://funstat.info/api/v1/users/{user_id}/stats_min"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {JWT}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return jsonify({"success": False, "error": "Failed to fetch user info", "code": response.status_code}), 500
        
        data = response.json()
        return jsonify({"success": True, "data": data})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
