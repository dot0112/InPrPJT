from fastapi import APIRouter
from .endpoints import select, stats, counts

router = APIRouter()
router.include_router(stats.router)
router.include_router(counts.router)
router.include_router(select.router)
