# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,temp, list1, list2):
        
        if list1 and list2: 
            if list1.val <= list2.val:
                temp.next = list1
                self.merge(temp.next,list1.next,list2)
            else:
                temp.next = list2
                self.merge(temp.next,list1,list2.next)
                
        
        elif list1:
            temp.next = list1
            return temp
        elif list2:
            temp.next = list2
            return temp
        elif not list1 and not list2:
            temp.next = None
            return temp
        return temp
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans =ListNode()
        ans = self.merge(ans,list1,list2)
        return ans.next
        
        
        
        
#         ans = ListNode()
#         temp = ans
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 temp.next = list1
#                 list1 = list1.next
#             else:
#                 temp.next = list2
#                 list2 = list2.next
#             temp = temp.next
        
#         if list1:
#             temp.next = list1
#         else:
#             temp.next = list2
#         return ans.next