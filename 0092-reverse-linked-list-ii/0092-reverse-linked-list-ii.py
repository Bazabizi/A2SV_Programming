# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if left < right:
            front = ListNode()
            front.next = head
            current = head
            idx = left
            while idx > 1:
                current = current.next
                front = front.next
                idx -= 1
            tail = current
            previous = front
            nex = current.next
        #reverse
            size = right-left
            
            while size >= 0 :
                current.next = previous
                previous = current
                current  = nex
                if nex:
                    nex = nex.next
                size -= 1
            front.next = previous
            tail.next = current
            if left == 1:
                return previous
        return dummy.next