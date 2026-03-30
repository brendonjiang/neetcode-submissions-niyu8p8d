class ListNode:
    def __init__(self, id=None, val=None, next=None, prev=None):
        self.id = id
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.myCache = {}
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.myCache:
            node = self.myCache[key]

            self.remove(node)
            self.add(node)

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.myCache:
            node = self.myCache[key]

            self.remove(node)
            self.add(node)
            node.val = value

        else:
            self.size += 1

            if self.size > self.capacity:
                remove = self.head.next
                self.remove(remove)
                self.myCache.pop(remove.id)

            node = ListNode(id=key, val=value)
            self.add(node)
            self.myCache[key] = node
                

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def add(self, node):
        top_node = self.tail.prev

        top_node.next, node.prev = node, top_node
        node.next, self.tail.prev = self.tail, node

