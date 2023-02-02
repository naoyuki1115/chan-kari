from fastapi import APIRouter

router = APIRouter(
    prefix="/rentals",
)


@router.get("")
def list():
    pass
