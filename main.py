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


def check_value(value):
    return True if str(value).isdigit() else False


def guess_number():
    random_number = randint(1, 10)

    while True:

        try:
            user_number = int(input())
        except ValueError:
            print("Нужно ввести число от 1 до 10.")
            continue

        if user_number < 1 or user_number > 10:
            print("Вы ввели число вне диапазона [1; 10], попробуйте еще раз.")
            continue

        elif user_number == random_number:
            print(f"Угадал! Это было число {random_number}. Поздравляю с победой!")
            break

        elif user_number < random_number:
            print("Слишком мало, попробуй еще раз.")
            continue

        elif user_number > random_number:
            print("Слишком много, попробуй еще раз.")
            continue


if __name__ == "__main__":
    print("Привет! Я загадаю число от 1 до 10, а тебе нужено будет его угадать. Удачи! :)")
    time.sleep(1)
    print("Введи число от 1 до 10.")

    guess_number()







