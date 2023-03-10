# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        ans = []
        for node in lists:
            while node :
                ans.append(node.val)
                node = node.next
        
        ans.sort()
        for val in ans:
            head.next = ListNode(val)
            head = head.next
        
        return dummy.next
        