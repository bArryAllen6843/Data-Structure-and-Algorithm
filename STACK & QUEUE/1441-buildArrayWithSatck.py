class Solution:
    def build(self,target, n):
        res = []
        s = set(target)
        for i in range(1, target[-1] + 1):
            res.append("Push")
            if i not in s:
                res.append("Pop")
        return res


if __name__ == '__main__':
    target = [1, 3]
    n = 3
    a = Solution()
    print(a.build(target, n))
