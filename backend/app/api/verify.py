from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from app.services.attestation import AttestationService

router = APIRouter()

attestor = AttestationService()


class VerifyRequest(BaseModel):
    attestation: Dict[str, Any]


@router.post("/verify")
def verify_attestation(req: VerifyRequest):
    return attestor.verify_attestation(req.attestation)