# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,pre,head):
            if not head:
                return pre
            nex= head.next
            head.next = pre
            pre = head
            return self.reverse(head,nex)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr= head
        nex = None
        if not head:
            return head
        return self.reverse(pre,curr)  

    
#         while curr!=None:
#             nex= curr.next
#             curr.next = pre
#             pre = curr
#             curr = nex
#         return pre

#         if not head.next:  
#             return head
        
        