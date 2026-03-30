# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        output = link = ListNode(next=head)
        start, cur = head, head

        counter = 0

        while cur:
            counter += 1

            if counter % k == 0:
                prev = cur.next
                end = cur
                cur = start

                link_temp = start
                while cur != end:
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                
                link.next = cur
                link = link_temp

                start = cur.next
                cur.next = prev
                cur = start
                counter += 1
                
                if not cur:
                    return output.next

            cur = cur.next


        return output.next