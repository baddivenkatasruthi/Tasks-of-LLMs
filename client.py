from models.user import User


class TestUser(User):

    def display_dashboard(self) -> None:
        print(f"User Dashboard: {self.name} (ID: {self.user_id})")

    def can_borrow_books(self) -> bool:
        return True


def main():
    u1 = TestUser("Sruthi", "1235356")
    print("User Name:", u1.name)
    print("User ID:", u1.user_id)
    u1.display_dashboard()


if __name__ == "__main__":
    main()