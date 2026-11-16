from app import App
from services.user_service import UserService, UserInputError, AuthenticationError
from repositories.user_repository import UserRepository
from stub_io import StubIO


class AppLibrary:

    def __init__(self):
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)
        self._io = StubIO()
        self._app = App(self._user_service, self._io)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if value not in outputs:
            raise AssertionError(f'"{value}" not found in outputs {outputs}')

    def run_application(self):
        self._app.run()