# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            left = head
            right = head.next
            while right :
                if left.val == right.val:
                    right = right.next
                else:
                    left.next = right
                    left = right
            left.next = right
        return head
                    