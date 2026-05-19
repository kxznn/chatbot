import requests

url = "http://localhost:7860/api/v1/run/86a92e6b-d5c5-4933-911e-2e7e9e2409d9"

payload = {
"input_value": "Qual o horário de funcionamento do petshop?",
"output_type": "chat",
"input_type": "chat"
}

headers = {
"Content-Type": "application/json"
}

try:
response = requests.post(
url,
json=payload,
headers=headers
)

```
response.raise_for_status()

print(response.text)
```

except requests.exceptions.RequestException as e:
print(f"Erro ao acessar API: {e}")

except ValueError as e:
print(f"Erro ao processar resposta: {e}")
