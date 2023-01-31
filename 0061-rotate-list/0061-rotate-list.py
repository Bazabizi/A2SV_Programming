# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        if head :
            while temp:
                temp= temp.next
                count +=1
            rotate = k % count
        
            while rotate > 0 :
                tail = head
                pre = head
                tail = tail.next
                while tail.next:
                    tail = tail.next
                    pre = pre.next
                tail.next = head
                pre.next = None
                head = tail
                rotate -= 1
        return head
            