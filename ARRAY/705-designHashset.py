class MyHashSet:

    def __init__(self):
        self.s=set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.s:
            return True
        else:return False


if __name__ == '__main__':

    obj = MyHashSet()
    obj.add(2)
    obj.add(5)
    obj.add(8)
    obj.remove(5)
    param_3 = obj.contains(6)
    print(param_3)