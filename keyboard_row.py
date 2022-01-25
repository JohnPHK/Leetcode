from typing import List


def iterateHelper(word: str, keyboard_row: str) -> bool: 
    for ch in word:
        if ch not in keyboard_row:
            return False
    return True


def findWords(words: List[str]) -> List[str]:
    first_row = "qwertyuiopQWERTYUIOP"
    second_row = "asdfghjklASDFGHJKL"
    third_row = "zxcvbnmZXCVBNM"
    to_return = []

    for word in words:
        if iterateHelper(word, first_row):
            to_return.append(word)

        if iterateHelper(word, second_row):
            to_return.append(word)

        if iterateHelper(word, third_row):
            to_return.append(word)

    return to_return
        


if __name__ == "__main__":
    print(findWords(["Hello","Alaska","Dad","Peace"]))

