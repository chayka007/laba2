"""Игра «Угадай число»."""
import random


def guess_the_number(lower=1, upper=100):
    secret = random.randint(lower, upper)
    attempts = 0

    print(f"Загадано число от {lower} до {upper}. Попробуйте угадать!")
    while True:
        guess = int(input("Ваше число: "))
        attempts += 1
        if guess < secret:
            print("Больше!")
        elif guess > secret:
            print("Меньше!")
        else:
            print(f"Угадали за {attempts} попыток!")
            break


if __name__ == "__main__":
    guess_the_number()
