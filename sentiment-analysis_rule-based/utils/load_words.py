from typing import List, Tuple


def load_words(filename: str) -> Tuple[List[str], List[str]]:
    """Memuat kata positif dan negatif dari file."""
    positive_words: List[str] = []
    negative_words: List[str] = []
    current_list = None

    with open(file=filename, mode='r') as file:
        for line in file:
            line = line.strip().lower()
            if line == "positif:":
                current_list = positive_words
            elif line == "negatif:":
                current_list = negative_words
            elif line and current_list is not None:
                current_list.append(line)

    return positive_words, negative_words
