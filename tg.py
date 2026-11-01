import requests

key = "API"
chat_id = "chat_id"

url = f"https://api.telegram.org/bot{key}/sendMessage"

message = "Hello! Your inventory bot is working."

response = requests.post(url, data={"chat_id": chat_id, "text": message})

print(response.status_code)
print(response.json())
