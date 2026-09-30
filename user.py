from abc import ABC, abstractmethod


class User(ABC):

    @staticmethod
    def generate_unique_id() -> str:
        return "0"

    def __init__(self, name: str = "", contact_info: str = ""):
        self._user_id = User.generate_unique_id()
        self._name = name
        self._contact_info = contact_info

    @classmethod
    def copy_of(cls, other_user):
        return cls(name=other_user.name, contact_info=other_user.contact_info)

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value: str):
        self._contact_info = value

    @abstractmethod
    def display_dashboard(self) -> None:
        pass

    @abstractmethod
    def can_borrow_books(self) -> bool:
        pass