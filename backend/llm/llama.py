import requests

def call_llama(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']
