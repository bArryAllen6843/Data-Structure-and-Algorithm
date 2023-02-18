def addStrings(num1: str, num2: str) -> str:
    l1, l2 = len(num1), len(num2)
    a = b = 0

    for i in range(l1):
        r = ord(num1[i]) - 48
        a = a * 10 + r
    for i in range(l2):
        s = ord(num2[i]) - 48
        b = b * 10 + s
    return str(a + b)


if __name__ == '__main__':
    s1 = "10"
    s2 = "123"
    print(addStrings(s1, s2))
