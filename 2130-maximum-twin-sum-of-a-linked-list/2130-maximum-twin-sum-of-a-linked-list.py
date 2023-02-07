# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        ans = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = None
        cur = slow
        nex = slow
        
        while nex :
            nex = cur.next
            cur.next = tail
            tail = cur
            cur = nex
        
        while head and tail:
            twinSum = head.val + tail.val
            ans = max(ans,twinSum)
            head = head.next
            tail = tail.next
        
        return ans