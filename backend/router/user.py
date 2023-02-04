from fastapi import APIRouter, status
from router import owned_item, rental

router = APIRouter(
    prefix="/users",
)

router.include_router(owned_item.router)
router.include_router(rental.router)


@router.get("/profile")
def profile():
    # Mock
    return {
        "name": "user name",
        "nickName": "nick name",
        "email": "example@mail.com",
        "imageUrl": "http://example.com/test.png",
    }


@router.put("/profile", status_code=status.HTTP_204_NO_CONTENT)
def change_nickname():
    pass
