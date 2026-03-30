# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        cur = ListNode()
        cur.next = head

        while cur.next:
            length += 1
            cur = cur.next
        
        if length == 1:
            return

        steps = length - n

        dummy = cur = ListNode()
        cur.next = head
        for i in range(steps):
            cur = cur.next

        if cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        return dummy.next