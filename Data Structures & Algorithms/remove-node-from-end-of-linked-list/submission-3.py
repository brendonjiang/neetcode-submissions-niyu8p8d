# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        n = length - n

        counter = 0

        dummy = cur = ListNode(next=head)
        while cur.next:
            if counter == n:
                cur.next = cur.next.next
                return dummy.next
            counter += 1
            cur = cur.next

        return dummy.next