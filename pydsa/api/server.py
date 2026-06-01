from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

# Import your core engine wrapper
from pydsa import solve as _solve, search as _search
from pydsa.core.exceptions import PyDSAError

app = FastAPI(
    title="PyDSA Engine API",
    description="Semantic AI routing and execution for DSA problems.",
    version="0.1.0"
)

# 1. Define the Request Data Model
class SolveRequest(BaseModel):
    query: str
    inputs: list[Any] = []
    trace: bool = False

# 2. Define the Endpoints
@app.post("/solve")
async def solve_problem(req: SolveRequest):
    try:
        # Pass the web request straight into your engine
        result = _solve(req.query, *req.inputs, trace=req.trace)
        
        # FastAPI automatically converts your dataclass into clean JSON
        return result
        
    except PyDSAError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

@app.get("/search")
async def search_problems(q: str, limit: int = 10):
    problems = _search(q, limit=limit)
    return {"results": problems}

@app.get("/health")
async def health_check():
    return {"status": "online", "engine": "ready"}