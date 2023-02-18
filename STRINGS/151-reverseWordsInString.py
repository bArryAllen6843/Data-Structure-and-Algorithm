def reverseWords(s: str) -> str:
    sList = s.split()
    n = len(sList) - 1
    output = ""
    while n >= 0:
        output += " " + sList[n]
        n -= 1
    a=output.strip()
    return a


if __name__ == '__main__':
    # st = "the sky is blue"
    st="a good   example"
    print(reverseWords(st))

