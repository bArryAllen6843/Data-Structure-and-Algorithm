import collections


class Solution:
    # row and column are dictionaries containing each row  or column as key and list of column or row as value
    # for any particular row if there exists a column in points set then remove that stone
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in row[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in column[j]:
                if (x, j) in points:
                    dfs(x, j)

        points, island, row, column = {(i, j) for i, j in stones}, 0, collections.defaultdict(
            list), collections.defaultdict(list)
        for i, j in stones:
            row[i].append(j)
            column[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island


if __name__ == '__main__':
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    a = Solution()
    print(a.removeStones(stones))
