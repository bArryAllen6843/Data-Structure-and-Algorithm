import collections


class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x: int) -> None:
        q = self._queue
        q.append(x)
        for i in range(len(q) - 1):
            q.append(q.popleft())
        return q

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not len(self._queue)


if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)