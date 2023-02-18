def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t): return False
    if len(s) == 0:
        return True
    subSeq = 0
    for i in range(len(t)):
        if subSeq <= len(s) - 1:
            if s[subSeq] == t[i]:
                subSeq += 1
    return len(s) == subSeq


if __name__ == '__main__':

    s = "abc"
    t = "axbvhc"
    print(isSubsequence(s, t))
