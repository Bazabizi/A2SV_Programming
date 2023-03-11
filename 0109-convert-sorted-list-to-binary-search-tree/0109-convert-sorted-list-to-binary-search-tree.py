# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self,left , right, arr):
        if right < left:
            return None
        mid = left + (right- left) //2
        tree = TreeNode(arr[mid])
        tree.left = self.merge(left , mid - 1 , arr)
        tree.right = self.merge(mid + 1 , right , arr)
        return tree
    
    
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        left = 0
        right = len(nums) - 1
        
        return self.merge(left,right ,nums)