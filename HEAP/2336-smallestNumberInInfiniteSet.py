import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        self.index=1

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.index+=1
        return self.index-1

    def addBack(self, num: int) -> None:
        if self.index > num and num not in self.heap:
            heapq.heappush(self.heap, num)


if __name__ == '__main__':

    obj = SmallestInfiniteSet()
    param_1 = obj.popSmallest()
    print(param_1)
    param_2 = obj.popSmallest()
    print(param_2)
    param_3 = obj.popSmallest()
    print(param_3)
    obj.addBack(4)
    obj.addBack(2)