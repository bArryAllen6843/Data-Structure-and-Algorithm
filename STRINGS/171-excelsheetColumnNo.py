def columnNo(s):
    ans, pos = 0, 0
    for letter in reversed(s):
        digit = ord(letter) - 64
        ans += digit * 26 ** pos
        pos += 1
    return ans


if __name__ == '__main__':
    st = 'AB'
    print(columnNo(st))
