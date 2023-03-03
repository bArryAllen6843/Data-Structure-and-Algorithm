class Solution:
    def combination2(self, candidate, target):
        res = []
        candidate.sort()
        self.dfs(candidate, target, [], res)
        return res

    def dfs(self, candidate, target, paths, res):
        if target < 0:
            return
        if target == 0:
            res.append(paths)

        for i in range(len(candidate)):
            if i > 0 and candidate[i] == candidate[i - 1]:
                continue

            if candidate[i] > target:
                break

            self.dfs(candidate[i + 1:], target - candidate[i], paths + [candidate[i]], res)


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    a = Solution()
    print(a.combination2(candidates, target))
