def isIsomorphic(s, t):
    # method-1
    # return [[*map(s.index, s)] == [*map(t.index, t)]]

    # method-2
    map1 = []
    map2 = []

    for idx in s:
        map1.append(s.index(idx))  # s.index(idx) will only give first occurence of that idx(substring)
    for idx in t:
        map2.append(t.index(idx))

    if map1 == map2:
        return True
    return False


if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))
