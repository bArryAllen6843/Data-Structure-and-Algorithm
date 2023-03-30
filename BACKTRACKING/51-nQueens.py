class Solution:
    def solveNQueens(self, n: int):
        def DFS(queens, xy_diff, xy_sum):
            p=len(queens)  # p:row
            if p==n:
                result.append(queens)
                return None
            for q in range(n):  # q: column
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])

        result=[]
        DFS([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


if __name__ == '__main__':
    a=Solution()
    print(a.solveNQueens(4))