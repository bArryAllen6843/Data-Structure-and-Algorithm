def isValid(s: str) -> int:
    st = []
    m = {"(": ")", "[": "]", "{": "}"}

    for el in s:
        if el in m:
            st.append(el)
        else:
            if len(st) == 0:
                return 0
            elif m[st[-1]] == el:
                st.pop()
            else:
                return 0
    return 1 if len(st) == 0 else 0


if __name__ == '__main__':
    strs = "()({[]}{}))"
    print(isValid(strs))
