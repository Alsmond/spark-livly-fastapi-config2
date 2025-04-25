from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json

app = FastAPI()

LIVY_URL = "http://ec2-34-236-36-186.compute-1.amazonaws.com:8998"

class CodeExecutionRequest(BaseModel):
    session_id: int
    code: str

@app.get("/")
def read_root():
    return {"message": "FastAPI is running 🚀"}

@app.post("/execute")
def execute_code(request: CodeExecutionRequest):
    payload = {"code": request.code}
    try:
        response = requests.post(
            f"{LIVY_URL}/sessions/{request.session_id}/statements",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return {"output": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error submitting code to Livy")

@app.get("/result/{session_id}/{statement_id}")
def get_result(session_id: int, statement_id: int):
    try:
        response = requests.get(f"{LIVY_URL}/sessions/{session_id}/statements/{statement_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error fetching result from Livy")
