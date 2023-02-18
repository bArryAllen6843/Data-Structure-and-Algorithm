def f(paragraph, banned):
    for ch in "!?',;.": paragraph = paragraph.replace(ch," ")

    res, d, cnt = "", {}, 0

    for word in paragraph.lower().split(" "):
        if word in banned:
            continue
        elif word in d:
            d[word] += 1
        else:
            d[word] = 1
        if d[word] > cnt:
            cnt = d[word]
            res = word
    return res


if __name__ == '__main__':
    p = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(f(p, banned))
