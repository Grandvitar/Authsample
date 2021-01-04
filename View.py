import Models.System
def UI():
    system1 = Models.System.System('Lesson6')
    while True:
        choise = int(input('Введите 1 для регистрации, 2 для авторизации, 3 для выхода из аккаунта, 4 для завершения программы'))
        if choise == 1:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            flag = system1.registration(a,b)
            if flag:
                print('Вы успешно зарегистрированы')
            else:
                print('Ошибка регистрации')
        elif choise == 2:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            flag = system1.authorisation(a, b)
            if flag:
                print('Вход выполнен')
            else:
                print('Ошибка входа')
        elif choise == 3:
            flag = system1.log_out()
            if flag:
                print('Выход выполнен')
            else:
                print('Ошибка выхода')
        elif choise == 4:
            break





