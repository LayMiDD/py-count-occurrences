def count_occurrences(phrase: str, letter: str) -> int:
    if letter == '':
        return 0
    return phrase.lower().count(letter.lower())