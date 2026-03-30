# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        l1 = head.next
    
        prev, cur = None, l2

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        l2 = prev

        cur = head
        while l1 and l2:
            cur.next = l2
            cur = l2
            l2 = l2.next

            cur.next = l1
            cur = l1
            l1 = l1.next

        while l1:
            cur.next = l1
            cur = l1
            l1 = l1.next


