# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,prefix , count , target):
        if not root:
            return
        prefix += root.val
        if prefix - target in count:
            self.ans += count[prefix - target]
        count[prefix] += 1
        self.traverse(root.left,prefix ,count.copy(), target)
        self.traverse(root.right,prefix ,count.copy(), target)
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        self.ans = 0
        self.traverse(root,0 , count , targetSum)
        return self.ans