# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,level , n):
        if not root:
            return 
        self.order[level].append(n)
        self.traverse(root.left , level + 1,2*n + 1)
        self.traverse(root.right , level + 1 , 2*n + 2)
        
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.order = defaultdict(list)
        self.traverse(root , 0 , 0)
        maxVal = 0
        for distance in self.order.values():
            left = distance[0]
            right = distance[-1]
            maxVal = max(right - left + 1 , maxVal)
        return maxVal