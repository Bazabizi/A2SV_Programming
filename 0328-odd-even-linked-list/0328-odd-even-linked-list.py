# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        tempOdd = odd
        even = ListNode()
        tempEven = even
        while head:
            if head:
                tempOdd.next = head
                tempOdd = tempOdd.next
                head= head.next
            if head:    
                tempEven.next = head
                tempEven = tempEven.next
                head = head.next
                
        
        tempOdd.next = even.next
        tempEven.next =None
        return odd.next