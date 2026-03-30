class ListNode:
    def __init__(self, id=None, val=None, next=None, prev=None):
        self.id = id
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.myCache = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.myCache:
            node = self.myCache[key]
            if self.size == 1:
                return self.myCache[key].val

            # move node from original position
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            # add node to beginning
            first_node = self.tail.prev
            first_node.next = node
            node.prev = first_node
            node.next = self.tail
            self.tail.prev = node

            return self.myCache[key].val

        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.myCache:
            node = self.myCache[key]

            if self.size == 1:
                self.myCache[key].val = value
                return

            # move node from original position
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            # add node to beginning
            first_node = self.tail.prev
            first_node.next = node
            node.prev = first_node
            node.next = self.tail
            self.tail.prev = node

            # change node val
            node.val = value
            return

        else:
            self.size += 1

            if self.size > self.capacity:
                # remove last node from LL and cache
                last_node = self.head.next
                self.myCache.pop(last_node.id)

                second_node = self.head.next.next
                self.head.next = second_node
                second_node.prev = self.head

            # add new node to beginning of LL
            node = ListNode(id=key, val=value)
            first_node = self.tail.prev
            first_node.next = node
            node.prev = first_node
            node.next = self.tail
            self.tail.prev = node
            
            self.myCache[key] = node
            return
