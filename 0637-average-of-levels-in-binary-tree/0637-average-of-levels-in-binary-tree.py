# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root]) 
        ans = []
        
        while queue:
            size = len(queue)
            temp = 0
            
            for _ in range(size):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            temp /= size
            ans.append(temp)
        
        return ans