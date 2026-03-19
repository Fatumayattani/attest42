from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from app.services.pipeline import Attest42Pipeline

router = APIRouter()

pipeline = Attest42Pipeline()


class RunRequest(BaseModel):
    input_data: str
    policy: Dict[str, Any]


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/run")
def run_pipeline(req: RunRequest):
    return pipeline.run(req.input_data, req.policy)