from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def list():
    pass