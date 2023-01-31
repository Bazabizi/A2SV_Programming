# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        fast = head
        slow = ListNode
        slow.next= head
        head = slow
        idx = 0
        while idx < n:
            fast=fast.next
            idx +=1
        while fast!=None:
            slow = slow.next
            fast = fast.next
        if slow.next != None:
            slow.next = slow.next.next
        return head.next