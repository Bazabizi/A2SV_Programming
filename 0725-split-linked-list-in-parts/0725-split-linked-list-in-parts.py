# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        ans = []
        rem = count % k
        contain = count //k
        
        for idx in range(k):
            ans.append(head)
            num = contain
            if rem > 0:
                num += 1
                rem -= 1
            while head and num > 1:
                head = head.next
                num -= 1
            
            if head:
                temp = head
                head = head.next
                temp.next = None
        
        return ans
                    