from typing import Optional


class User:
    __id: Optional[int]
    __uid: str
    __name: str
    __email: str
    __image_url: Optional[str] = None

    def __init__(
        self,
        uid: str,
        name: str,
        email: str,
        image_url: Optional[str] = None,
        id: Optional[int] = None,
    ):
        self.__id = id
        self.__uid = uid
        self.__name = name
        self.__email: str = email
        self.__image_url: Optional[str] = image_url
