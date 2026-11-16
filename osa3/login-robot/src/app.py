from entities.user import User


class App:

    def __init__(self, user_service, io):
        self._user_service = user_service
        self._io = io

    def run(self):
        while True:
            command = self._io.read("komento: ")

            if command == "":
                break

            if command == "new":
                username = self._io.read("username: ")
                password = self._io.read("password: ")

                try:
                    self._user_service.create_user(username, password)
                    self._io.write("New user created")
                except Exception as error:
                    self._io.write(str(error))

            elif command == "login":
                username = self._io.read("username: ")
                password = self._io.read("password: ")

                try:
                    self._user_service.check_credentials(username, password)
                    self._io.write("Logged in")
                except Exception as error:
                    self._io.write(str(error))
                    