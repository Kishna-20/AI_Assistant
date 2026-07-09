from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app1 = FastAPI()

class ChatRequest(BaseModel):
    message : str

@app1.post("/chat")
def chat(request: ChatRequest):
    response = ollama.chat(
        model = "llama3.2",
        messages = [
            {
                "role": "user",
                "content": request.message,
            }
        ]
    )

    return{
        "reply":response["message"]["content"]
    }
