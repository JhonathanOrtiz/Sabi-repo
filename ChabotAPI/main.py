from fastapi import FastAPI
from typing import Optional
import requests
from app import create_app
from app.send_message import get_response
from app.models import Query
from app.parsing_response import parse_response

app = create_app()

@app.get('/')
def read_root():
    return {"Hello": 'World'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post('/webhook')
def send_request(query: Query):

    if query.audio is not None:
        audio = query.audio
        session_id = query.session_id
        response, next_session = get_response(audio=audio, session_id=session_id)
        response = parse_response(response)
        return {"response": response, "session_id":next_session}
    
    texto = query.text
    session_id = query.session_id
    response, next_session = get_response(texto, session_id=session_id)
    response = parse_response(response)
    return {"response": response, "session_id": next_session}

    
    
