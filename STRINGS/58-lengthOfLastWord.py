def lengthOfLastWord(s: str) -> int:
    # ss = s.strip()
    # a = ss.split(" ")
    # return len(a[-1])
    a=len(s.split()[-1])
    return a


if __name__ == '__main__':
    str = "   fly me   to   the moon  "
    print(lengthOfLastWord(str))
