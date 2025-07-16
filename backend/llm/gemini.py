import requests

def call_gemini(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": "AIzaSyCMLaAY5dQ0Dhjk_23GFl7ru9ImW7HIDvE"
    }
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    response = requests.post(url, headers=headers, params=params, json=data)
    try:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception:
        return "Gemini response parsing failed."
