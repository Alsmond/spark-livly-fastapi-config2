# Livy-FastAPI Server

This project allows you to execute Spark code on a remote Apache Livy server using a FastAPI backend.

## Features

- Submit code to an active Livy session.
- Fetch execution results.
- RESTful API endpoints for integration.

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- `GET /`: Health check.
- `POST /execute`: Submit code to a Livy session.
- `GET /result/{session_id}/{statement_id}`: Fetch result of a submitted code.

## Example Usage

```bash
curl -X POST http://localhost:8000/execute \
-H "Content-Type: application/json" \
-d '{"session_id": 0, "code": "1 + 2"}'
```

Then poll:

```bash
curl http://localhost:8000/result/0/{statement_id}
```
