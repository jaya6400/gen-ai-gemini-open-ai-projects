from fastapi import FastAPI, Body
from fastapi.responses import PlainTextResponse
from ollama import Client

app = FastAPI()
client = Client(host="http://localhost:11434")

@app.get("/")
def read_root():
    return {"message": "Hello, This is a starter to AI Ollama, FastAPI"}

@app.get("/contact-us")
def contact_us():
    return {"email": "dev@gmail.com"}

@app.post("/chat", response_class=PlainTextResponse)
def chat(message: str = Body(..., description="The Message")):
    response = client.chat(
        model="gemma:2b",
        messages=[{"role": "user", "content": message}]
    )
    content = getattr(response.message, "content", "").strip()
    return content
