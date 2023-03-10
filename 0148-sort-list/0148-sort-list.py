# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def midPoint(self,head):
        slow = head
        fast = head
        
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        mid = slow
        return mid
    
    def mergeSort(self,left ):
        if left.next:
            mid = self.midPoint(left)
            temp = mid
            mid = temp.next
            temp.next = None
            leftNode = self.mergeSort(left)
            rightNode = self.mergeSort(mid)
            return self.merge(leftNode , rightNode)
        return left
    
    def merge(self,temp1 , temp2):
        newNode = ListNode()
        dummy = ListNode()
        newNode = dummy
    
        while temp1  and temp2 :
            if temp1.val <= temp2.val:
                newNode.next = temp1
                temp1 = temp1.next
            else:
                newNode.next = temp2
                temp2 = temp2.next
            newNode = newNode.next
        if temp1:
            newNode.next = temp1
        if temp2 :
            newNode.next = temp2
          
        return dummy.next
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        while tail.next:
            tail = tail.next
        
        return self.mergeSort(head)