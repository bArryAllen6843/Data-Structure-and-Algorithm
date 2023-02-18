def twoSum(nums, target):
    m = {}
    for i, el in enumerate(nums):
        if target - el in m:
            return [m[target - el], i]
        m[el] = i


if __name__ == "__main__":
    # a = [2, 7, 11, 15]
    # a = [3, 3]
    a = [3, 2, 4]
    print(twoSum(a, 6))
