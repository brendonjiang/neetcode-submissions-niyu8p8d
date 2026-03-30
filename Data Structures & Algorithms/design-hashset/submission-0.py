class MyHashSet:

    def __init__(self):
        self.myArr = []

    def add(self, key: int) -> None:
        if key in self.myArr:
            return
        else:
            self.myArr.append(key)

    def remove(self, key: int) -> None:
        if key in self.myArr:
            self.myArr.remove(key)        
        else:
            return
    def contains(self, key: int) -> bool:
        if key in self.myArr:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)