def containsDuplicate(nums):
    s = set()
    i = 0
    while i < len(nums):
        if nums[i] not in s:
            s.add(nums[i])
            i+=1
        else:
            return True
    return False


if __name__ == '__main__':
    a = [1, 2, 3, 2]
    print(containsDuplicate(a))
