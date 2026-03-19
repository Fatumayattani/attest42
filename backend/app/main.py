from fastapi import FastAPI
from app.api.routes import router as routes_router
from app.api.verify import router as verify_router

app = FastAPI(title="Attest42 API")

app.include_router(routes_router)
app.include_router(verify_router)