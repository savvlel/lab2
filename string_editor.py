def add(*string):
    # возвращает слитую строку
    res = ''
    for i in string:
        res += str(i)
    return res


def capital(string):
    # возвращает строку с заглавной буквы
    if type(string) != str:
        raise ValueError('Введена не строка')
    return string.capitalize()


def up(string):
    # возвращает строку в верхнем регистре
    if type(string) != str:
        raise ValueError('Введена не строка')
    return string.upper()


def reverse(string):
    string = str(string)
    return string[::-1]

print(reverse('sd'))
print(reverse(34))
print(reverse(1.25))


