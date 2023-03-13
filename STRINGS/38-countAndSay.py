class Solution:
    def countAndSay(self, n: int):
        def cs(str_):
            res = ''
            str_ += '#'
            c = 1
            for i in range(len(str_) - 1):
                if str_[i] == str_[i + 1]:
                    c += 1
                    continue
                else:
                    res += str(c) + str_[i]
                    c = 1
            return res

        start = '1'
        for i in range(n - 1):
            start = cs(start)
        return start


if __name__ == '__main__':
    n = 4
    a = Solution()
    print(a.countAndSay(n))
