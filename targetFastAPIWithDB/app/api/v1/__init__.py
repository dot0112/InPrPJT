from fastapi import APIRouter
from .endpoints import select, stats

router = APIRouter()
router.include_router(stats.get_stats)
router.include_router(select.catch_all)
