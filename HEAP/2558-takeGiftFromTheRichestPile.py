import heapq
import math


class Solution:
    def pickGifts(self, gifts, k: int) -> int:

        # Approach-1(priority queue)
        heap = []                                                             # Example: gifts = [25,64,9,4,100] ; k = 4

        for g in gifts: heapq.heappush(heap, -g)                               # heap = [-100,-64,-25, -9,-4]

                                                                                #    g    isqrt(g)        heap
        g = -heapq.heappop(heap)                                                # –––––  ––––––––  –––––––––––––––––
                                                                                 #   100     10      [-64,-25, -9, -4]
        for _ in range(k):                                                          # 64      8      [-25,-10, -9, -4]
            g = -heapq.heappushpop(heap, -math.isqrt(g))                             # 10      3      [-10,- 8, -9, -4]
                                                                                 #     9             [- 8, -4, -5, -3]

        return g - sum(heap)                                                      # return 9 - sum(- 8, -4,-5,-3) = 29

        # Approach-2(brute force)
        # i=0
        # while i<k:
        #     gifts=sorted(gifts)
        #     gifts[-1]=math.floor(math.sqrt(gifts[-1]))
        #     i+=1
        # return sum(gifts)

if __name__ == '__main__':
    gifts = [25, 64, 9, 4, 100]
    k = 4
    a=Solution()
    print(a.pickGifts(gifts,k))