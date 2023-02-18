def plusOne(digits):
    carry = 1
    n = len(digits)-1
    while carry:

        digits[n] += carry
        k = digits[n] % 10
        digits[n] = k
        carry = digits[n] // 10
        n-=1
        if n<0:
            return [1]+digits
    return digits


if __name__ == '__main__':
    a = [9]
    print(plusOne(a))
