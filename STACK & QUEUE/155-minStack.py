class MinStack:

    def __init__(self):
        self.st=[]

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return min(self.st)


if __name__ == '__main__':

    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.push(4)
    obj.pop()
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.getMin()
    print(param_4)