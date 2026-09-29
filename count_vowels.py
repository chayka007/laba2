"""Подсчёт количества гласных букв в строке."""


def count_vowels(text):
    vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU")
    return sum(1 for char in text if char in vowels)


if __name__ == "__main__":
    phrase = input("Введите текст: ")
    print(f"Количество гласных: {count_vowels(phrase)}")
