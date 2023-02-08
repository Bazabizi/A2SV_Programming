# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        temp = dummy
        
        while head:
            check = True
            while head.next and head.val == head.next.val:
                head = head.next
                check = False
            if check:
                temp.next = head
                temp = temp.next
            
            if head:
                head= head.next
        temp.next = head
        return dummy.next
    