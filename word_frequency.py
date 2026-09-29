"""Подсчёт частоты слов в текстовом файле."""
import re
from collections import Counter


def word_frequency(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r"[a-zа-яё]+", text)
    return Counter(words)


if __name__ == "__main__":
    frequencies = word_frequency("sample.txt")
    for word, count in frequencies.most_common(10):
        print(f"{word}: {count}")
