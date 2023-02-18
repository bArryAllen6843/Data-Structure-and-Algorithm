def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        # if length of set is greater than one it means all the zipped strings having letter group not equal
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    # if strs is null
    else:
        return min(strs)


if __name__ == '__main__':
    # strs = ["flowers", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs))

