from collections import Counter

def singleNumber(nums):
    s = set(nums)
    l = list(s)
    d = l * 2
    sum1 = sum(d)
    sum2 = sum(nums)
    return sum1 - sum2
    # return sum(list(set(nums)) * 2) - sum(nums)

# method-2 using counter
def f(nums):
    a=dict(Counter(nums))
    b=[k for k,v in a.items() if v==1]
    return b[0]


if __name__ == '__main__':
    a = [2, 2, 1]
    print(singleNumber(a))
    print(f(a))