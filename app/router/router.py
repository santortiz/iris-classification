from fastapi import APIRouter
from app.router.routes.model import router as model_router


router = APIRouter()

router.include_router(model_router, prefix="/model")