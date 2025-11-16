from fastapi import FastAPI, Form
from backend.response_generator import ResponseGenerator

app = FastAPI(title="Real-Time Multilingual Query Handler")

response_gen = ResponseGenerator()

@app.post("/translate")
async def translate_endpoint(query: str = Form(...)):
    response = response_gen.generate_response(query)
    return response

@app.get("/")
async def root():
    return {"message": "Use POST /translate with form-data 'query' to translate queries to English."}
