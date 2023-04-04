import heapq


class Solution:
    def kWeakestRows(self, mat, k: int):
        m = len(mat)
        n = len(mat[0])
        count = 0

        # mat[i][j]==1 means a soldier or mat[i][j]==0 means a civilian
        i = j = 0
        heap = []
        while i < m:
            # if we found a soldier then we will count the soldiers until this case is achieved: [1,1,1,1,1] or
            # the next element in the row is a civilian then we insert the count of soldiers and its row number in heap
            if mat[i][j] == 1:
                count += 1
                if j == n - 1 or mat[i][j + 1] == 0:
                    heapq.heappush(heap, (count, i))
                j += 1
            # if this is the case: [0,0,0,0]
            elif j==0 and mat[i][j]==0:
                heapq.heappush(heap,(count,i))
            # if the j has incremented to more than column number or we have reached civilians
            if j == n or mat[i][j] == 0:
                i += 1
                j = 0
                count = 0

        ans = []
        for i in range(k):
            # here we are unfolding the tuple freq,row= (count,i). As we know when we pop from heap it will pop the min
            # count first and that's what we want (k rows with minimum soldiers)
            freq, row = heapq.heappop(heap)
            ans.append(row)
        return ans


if __name__ == '__main__':
    # mat = [[1, 1, 0, 0, 0],
    #        [1, 1, 1, 1, 0],
    #        [1, 0, 0, 0, 0],
    #        [1, 1, 0, 0, 0],
    #        [1, 1, 1, 1, 1]]
    # k = 3
    mat = [[1, 0], [0, 0], [1, 0]]
    k = 2
    a = Solution()
    print(a.kWeakestRows(mat, k))
