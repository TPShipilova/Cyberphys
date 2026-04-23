import requests
from fastapi import FastAPI
from pydantic import BaseModel

class SMSRequest(BaseModel):
    """ Модель запроса """
    sms_text: str

def analyze_spam_sms(msg: str) -> int:
    """ Основная функция проверки СМС сообщения на спам с обращением к ollama """
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:0.5b",
                "prompt": f"Определи, является ли следующее SMS спамом. Ответь только одной цифрой: 1 если спам, иначе 0, без дополнительного текста. Текст SMS: {msg}",
                "stream": False,
            },
            timeout=30
        )
        r.raise_for_status()
        r = r.json()
    except Exception as e:
        r = {"error": str(e)}

    if "error" in r:
        return 0
    
    try:
        return int(r.get("response", "0").strip())
    except Exception as e:
        return 0


app = FastAPI()


@app.post("/analyze")
async def analyze(req: SMSRequest):
    """ Обработчик запроса """
    result = analyze_spam_sms(req.sms_text)
    return {"result": result}
