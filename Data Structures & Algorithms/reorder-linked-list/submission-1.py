# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        start = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next


        prev, cur = None, slow.next
        slow.next = None
        l1 = head.next

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        
        l2 = prev
        cur = head

        while l1 and l2:
            cur.next = l2
            cur = l2
            l2 = l2.next

            cur.next = l1
            cur = l1
            l1 = l1.next

        cur.next = l1

