from collections import Counter


class Solution:
    def equalPairs(self, grid) -> int:
        pairs = 0
        # we are storing tuples of rows in cnt becoz when we zip and unpack from grid it gives tuples of columns
        cnt = Counter(tuple(row) for row in grid)
        for tpl in zip(*grid):
            pairs += cnt[tpl]
        return pairs


if __name__ == '__main__':
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    a = Solution()
    print(a.equalPairs(grid))
