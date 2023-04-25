import collections


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(1)
    print(param_1)

    param_2 = obj.ping(100)
    print(param_2)

    param_3 = obj.ping(3001)
    print(param_3)
    # CONFUSION
    param_4 = obj.ping(3002)
    print(param_4)
