class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, paths, res):
        if target < 0:
            return
        if target == 0:
            res.append(paths)
            return

        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], paths + [candidates[i]], res)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    a = Solution()
    print(a.combinationSum(candidates, target))
