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

    def get_user_id(self) -> int:
        if self.__id is None:
            raise
        return self.__id

    def get_uid(self) -> str:
        return self.__uid

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_image_url(self) -> Optional[str]:
        return self.__image_url

    def set_id(self, id):
        self.__id = id
