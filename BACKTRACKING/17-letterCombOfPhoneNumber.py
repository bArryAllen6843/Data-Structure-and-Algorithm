class Solution:
    def letterCombinations(self, digits: str):
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if len(digits) == 0:
            return res
        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, paths, res):
        if index >= len(nums):
            res.append(paths)
            return
        string1 = dic[nums[index]]

        for i in string1:
            self.dfs(nums, index + 1,dic, paths + i, res)


if __name__ == '__main__':
    digits = "23"
    a = Solution()
    print(a.letterCombinations(digits))
