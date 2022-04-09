def data(name, family, born, city, email, phone):
    """

    :param name: Имя пользователя
    :param family: Фамилия пользователя
    :param born: Дата рождения пользователя
    :param city: Город проживания пользователя
    :param email: email пользователя
    :param phone: Телефон пользователя
    :return: Возвращает приведенные выше данные в одной строке
    """
    print(f"Имя:{name}, Фамилия:{family}, Дата рождения:{born}, Город проживания:{city}, Почта:{email},"
          f" Телефон:{phone}")


data(name="Ваня", family="Иванов", born="2000", city="Москва", email="Vanya@mail.ru", phone="89109909990")
