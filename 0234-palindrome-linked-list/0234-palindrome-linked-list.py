# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast.next and fast.next.next!= None:
            fast = fast.next.next
            slow = slow.next
        pre = slow
        if fast.next:
            slow = slow.next
            fast = fast.next
        cur = slow
        if slow.next:
            nex = slow.next
            while nex:
                pre = slow
                slow = nex
                nex = nex.next
                slow.next  = pre
        
        while head!= cur:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        
        return True
            