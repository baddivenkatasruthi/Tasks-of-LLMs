from models.user import User


class Librarian(User):

    def __init__(
        self, name=None, contact_info=None, employee_number: str = ""
    ):
        super().__init__(name, contact_info)
        self._employee_number = employee_number

    @property
    def employee_number(self) -> str:
        return self._employee_number

    @employee_number.setter
    def employee_number(self, value: str):
        self._employee_number = value

    def display_dashboard(self):
        print("----Librarian Dashboard------")
        print(f"Name : {self.name}")
        print(f"Employee #: {self._employee_number}")

    def can_borrow_books(self) -> bool:
        return True

    def add_new_book(self, book):
        pass

    def remove_book(self, book):
        pass