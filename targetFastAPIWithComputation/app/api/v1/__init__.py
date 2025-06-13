from fastapi import APIRouter
from .endpoints import stats, counts, computation

router = APIRouter()
router.include_router(stats.router)
router.include_router(counts.router)
router.include_router(computation.router)
