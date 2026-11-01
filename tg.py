import requests

key = "8561674482:AAFZf71l5ZrKOz1HTE04gaii5g5kzjDUpGk"
chat_id = "7600393647"

url = f"https://api.telegram.org/bot{key}/sendMessage"

message = "Hello! Your inventory bot is working."

response = requests.post(url, data={"chat_id": chat_id, "text": message})

print(response.status_code)
print(response.json())
