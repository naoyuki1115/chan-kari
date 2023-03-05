from typing import Optional


class User:
    __id: int
    __name: str
    __email: str
    __image_url: Optional[str] = None

    def __init__(
        self,
        name: str,
        email: str,
        image_url: Optional[str] = None,
    ):
        self.__name: str = name
        self.__email: str = email
        self.__image_url: Optional[str] = image_url
