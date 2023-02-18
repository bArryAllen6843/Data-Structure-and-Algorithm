def f(s):
    count = 0
    stack = []
    for e in s:
        if e == 'b':
            stack.append(e)
        elif stack:
            stack.pop()
            count += 1
    return count

# method-2(DYNAMIC PROGRAMMING)
def f1(s):
    right_del=s.count('a')



if __name__ == '__main__':
    st = 'abaabaab'
    print(f(st))
