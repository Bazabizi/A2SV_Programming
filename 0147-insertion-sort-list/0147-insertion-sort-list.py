# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp= head.next
        nex = head
        dummy = ListNode()
        dummy.next= head
        while temp:
            last = temp.next
            if nex.val > temp.val:
                head = dummy
                while head.next and head.next.val < temp.val:
                    head = head.next
                nex.next = last
                temp.next = head.next
                head.next = temp
            else:
                nex = nex.next
            temp = last
        return dummy.next