from random import *


print("Добро пожаловать в числовую угадайку!")

def main_menu():
    try:
        print(f"\n{'Главное меню':*^20}",
              "1. Новая игра",
              "2. Выход", sep="\n")
        user_choes = int(input("Выберите пункт меню :"))

    except:
        print(f"\n{'Введите 1 или 2':-^20}")
        return main_menu()
    if user_choes == 1:
        return play_game()
    elif user_choes == 2:
        say_good_bay()
        exit()
    else:
        print("На текущий момент выбор возможен '1' или '2'....")
        return main_menu()



def is_valid(n):
    return n.isdigit() if n.isdigit() and 1 <= int(n) <= 100 else False

def say_good_bay():
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

def play_game():
    count = 1
    try:
        b = int(input('Введите число от 1 до Вашего числа :'))
    except:
        print("\nПожалуйста, введите целое число!\n")
        return play_game()
    num = randint(1, b)
    print("Число сгенерировано, Угадайте его!")
    while True:
        user = input(f"Попытка {count}: ")
        if is_valid(user):
            if int(user) == num:
                count += 1
                print("Вы угадали, поздравляю!",
                      f"Загаданное число: {num}", sep="\n")
                print(f"Колличество использованных попыток: {count - 1}")
                return main_menu()
            elif int(user) > num:
                print("Слишком много, попробуйте еще раз")
                count += 1
            else:
                print("Слишком мало, попробуйте еще раз")
                count += 1
        else:
            print(f"А может быть все-таки введем целое число от 1 до {b}?!")


if __name__ == "__main__":
    main_menu()

