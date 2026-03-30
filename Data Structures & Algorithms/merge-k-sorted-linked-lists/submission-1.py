# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()

        combined = []

        for i in range(len(lists)):
            node = lists[i]
            
            while node:
                combined.append(node.val)
                node = node.next

            
        heapq.heapify(combined)

        while combined:
            val = heapq.heappop(combined)
            cur.next = ListNode(val=val)
            cur = cur.next

        return dummy.next