def rotateString(s: str, goal: str) -> bool:
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False


if __name__ == '__main__':
    st = 'abcde'
    g = 'cdeab'
    print(rotateString(st, g))
