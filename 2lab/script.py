import requests

sms_text = input("Введите текст SMS: ")
try:
    res = requests.post(f"http://localhost:8888/analyze", json={"sms_text": sms_text})
    res.raise_for_status()
    out = res.json()
    print(f"Результат: {out['result']}")
except Exception as e:
    print(e)
