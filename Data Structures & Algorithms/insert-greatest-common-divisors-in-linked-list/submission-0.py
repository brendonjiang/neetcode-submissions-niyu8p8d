# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        cur = head

        while cur and cur.next:
            temp, val2 = cur.next, cur.next.val
            val1 = cur.val

            if val2 > val1:
                val1, val2 = val2, val1

            for i in range(val2, 0, -1):
                if val1 % i == 0 and val2 % i == 0:
                    break

            cur.next = ListNode(val=i)
            cur = cur.next
            cur.next = temp
            cur = cur.next

        return dummy.next

