from fastapi import APIRouter
from .endpoints import stats, computation

router = APIRouter()
router.include_router(stats.router)
router.include_router(computation.router)
