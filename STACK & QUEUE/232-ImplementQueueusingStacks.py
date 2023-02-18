from typing import List, Any


class MyQueue:

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x: int) -> list[Any]:
        self.in_stk.append(x)
        return self.in_stk

    def pop(self) -> int:
        self.peek()
        return self.out_stk.pop()

    def peek(self) -> int:
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self) -> bool:
        return not self.in_stk and not self.out_stk


if __name__ == '__main__':
    obj = MyQueue()
    print(obj.push(3))
    print(obj.push(4))
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
