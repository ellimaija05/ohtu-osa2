from entities.user import User


class UserRepository:

    def __init__(self):
        self._users = []

    def find_all(self):
        return self._users

    def find_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None

    def create(self, user):
        self._users.append(user)
        return user
    