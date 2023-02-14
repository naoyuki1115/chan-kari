from fastapi import APIRouter, status

router = APIRouter()


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
