from models.user import User


class Member(User):
    MAX_BORROW_LIMIT = 5

    def __init__(self, name=None, contact_info=None):
        super().__init__(name, contact_info)
        self._borrowed_books_count = 0

    @property
    def borrowed_books_count(self) -> int:
        return self._borrowed_books_count

    def display_dashboard(self):
        print("---Member Dashboard---")
        print(f"Name: {self.name}")
        print(f"Books borrowed: {self._borrowed_books_count}")

    def can_borrow_books(self) -> bool:
        return self._borrowed_books_count < Member.MAX_BORROW_LIMIT

    def increment_borrow_count(self):
        self._borrowed_books_count += 1

    def decrement_borrow_count(self):
        if self._borrowed_books_count > 0:
            self._borrowed_books_count -= 1