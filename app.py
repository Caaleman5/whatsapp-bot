from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import uvicorn
import os

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    msg_from = form.get("From")
    msg_body = form.get("Body")

    print(f"Mensaje recibido de {msg_from}: {msg_body}")

    # Respuesta de prueba
    response_message = f"Hola 👋, recibí tu mensaje: {msg_body}"
    return PlainTextResponse(response_message)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
