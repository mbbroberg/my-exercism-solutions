def reverse(text):
    # I read that text[::-1] is the fastest solution, but it's not terribly readable, so:
    return ''.join(reversed(text))