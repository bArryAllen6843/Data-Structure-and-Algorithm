class Solution:
    def pacificAtlantic(self, heights):
        if not heights: return []

        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # It will start traversal from (0,0) and if this tuple is not in set then add in set and move in all
        # four directions for that tuple. If we found a greater land height then now than same process will be applied
        # otherwise return back.
        # In this manner it will reach max height land and add all tuples of coordinates till that land
        # This process will be done:
        # 1. for each row with column=0 and column=cols-1
        # 2. for each column with row=0 and row=rols-1
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbours
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, pacific_visited)
            traverse(row, cols - 1, atlantic_visited)

        for col in range(cols):
            traverse(0, col, pacific_visited)
            traverse(rows - 1, col, atlantic_visited)
        # the common tuples from both the sets will be added in the list
        return list(pacific_visited & atlantic_visited)


if __name__ == '__main__':
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    a = Solution()
    print(a.pacificAtlantic(heights))
