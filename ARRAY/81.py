def search(nums, target) -> bool:
    s = set()
    for i in range(len(nums)):
        if nums[i] not in s:
            s.add(nums[i])
            if target in s:
                return True
    return False


if __name__ == '__main__':
    a = [2, 5, 6, 0, 0, 1, 2]
    k = 0
    print(search(a, k))
