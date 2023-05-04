# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heap = []
        for node in lists:
            if node:
                heappush(heap , node)
        dummy = ListNode(0)
        temp = dummy
        while heap:
            node = heappop(heap)
            temp.next = node
            if node.next:
                heappush(heap, node.next)
            temp = temp.next
        
        return dummy.next