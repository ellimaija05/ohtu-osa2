from app import App
from services.user_service import UserService
from repositories.user_repository import UserRepository
from stub_io import StubIO


def main():
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    io = StubIO()
    app = App(user_service, io)
    app.run()


if __name__ == "__main__":
    main()
    