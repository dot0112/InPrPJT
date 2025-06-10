from fastapi import APIRouter
from .endpoints import select, stats

router = APIRouter()
router.include_router(stats.router)
router.include_router(select.router)
