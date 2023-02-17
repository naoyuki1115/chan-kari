from fastapi import APIRouter
from router import item, owned_item, rental, user

router = APIRouter()


@router.get("/test")
def list_item() -> None:
    print("test")


router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(item.router, prefix="/items", tags=["items"])
router.include_router(owned_item.router, prefix="/users/items", tags=["owned_items"])
router.include_router(rental.router, prefix="/users/rentals", tags=["rentals"])
