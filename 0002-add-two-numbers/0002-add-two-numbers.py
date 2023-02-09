# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        temp = ans
        while l1 and l2:
            node = ListNode()
            total = carry + l1.val + l2.val
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            node.val = total
            temp.next = node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            node = ListNode()
            total = carry + l1.val
            if total > 9:
                carry = 1
                total -=10
            else:
                carry = 0
            node.val = total
            temp.next = node
            temp = temp.next
            l1 = l1.next
            
        while l2:
            node = ListNode()
            total = carry + l2.val
            if total > 9:
                carry = 1
                total -=10
            else:
                carry = 0
            node.val = total
            temp.next = node
            temp = temp.next
            l2 = l2.next
        
        if carry == 1:
            node = ListNode(1)
            temp.next = node
        
        return ans.next
            