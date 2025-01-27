# Описание проекта: программа генерирует случайное число в диапазоне
# от 1 до 10 и просит пользователя угадать это число.

# Если догадка пользователя больше случайного числа, то программа должна
# вывести сообщение 'Слишком много, попробуйте еще раз'.

# Если догадка меньше случайного числа, то программа должна вывести
# сообщение 'Слишком мало, попробуйте еще раз'.

# Если пользователь угадывает число, то программа должна поздравить
# его и вывести сообщение 'Вы угадали, поздравляем!'.


from random import randint
import time


def guess_number():
    print("Привет! Я загадаю число от 1 до 10, а тебе нужено будет его угадать. Удачи! :)")
    random_number = randint(1, 10)
    time.sleep(1)
    print("Введите число:")

    while True:

        user_number = input()
        try:
            user_number = int(user_number)
        except ValueError:
            print("Нужно ввести число от 1 до 10.")
            continue

        if user_number < 1 or user_number > 10:
            print("Вы ввели число вне диапазона [1; 10], попробуйте еще раз.")
        elif user_number == random_number:
            print("Вы угадали, поздравляю с победой!")
            break
        elif user_number < random_number:
            print("Слишком мало, попробуйте еще раз.")
            continue
        elif user_number > random_number:
            print("Слишком много, попробуйте еще раз.")
            continue


guess_number()
