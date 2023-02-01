# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre = None
        cur = head
        nex = None
        #reverse the list
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        #compare
        head = pre
        while pre:
            tail = head
            while tail.next:
                if tail.val<x:
                    if tail.next.val >=x:
                        tail.val , tail.next.val = tail.next.val ,tail.val
                tail = tail.next
            pre = pre.next
            
        pre = None
        cur = head
        nex = None
        #reverse the list
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre