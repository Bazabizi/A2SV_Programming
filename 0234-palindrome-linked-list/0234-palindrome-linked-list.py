# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head
#         while fast.next and fast.next.next!= None:
#             fast = fast.next.next
#             slow = slow.next
#         pre = slow
#         if fast.next:
#             slow = slow.next
#             fast = fast.next
#         cur = slow
#         if slow.next:
#             nex = slow.next
#             while nex:
#                 pre = slow
#                 slow = nex
#                 nex = nex.next
#                 slow.next  = pre
        
#         while head!= cur:
#             if head.val != slow.val:
#                 return False
#             head = head.next
#             slow = slow.next
        
#         return True
# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = True
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        while prev and head:
            
            if head.val != prev.val:
                check = False
                break
                
            prev = prev.next
            head = head.next
        return check
            