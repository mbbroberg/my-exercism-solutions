def is_pangram(sentence: str) -> bool:
    pangram = "abcdefghijklmnopqrstuvwxyz"
    check = list(pangram)  # split single string into list of strings
    for l in check:
        if l not in sentence.lower():
            return False
    return True
