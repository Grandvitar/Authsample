import Models.User
class System:
    def __init__(self, name):
        self.__role = ['base', 'admin']
        admin = Models.User.User('admin', 'admin', self.__role[1])
        self.__name = name
        self.__list_users = [admin]
        self.__auth_user = None


    def registration(self, login, password):
        user = Models.User.User(login, password, self.__role[0])
        self.__list_users.append(user)
        self.__auth_user = user
        return True

    def authorisation(self, login, password):
        for user in self.__list_users:
            if login == user.login and password == user.password:
                self.__auth_user = user
                return True
        return False

    def edit_role(self, login, new_role):
        if self.__auth_user.role == 'admin':
            for user in self.__list_users:
                if login == user.login:
                    user.role = new_role
                    return True
        return False

    def log_out(self):
        if self.__auth_user is not None:
            self.__auth_user = None
            return True
        return False











