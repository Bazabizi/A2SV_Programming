# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []
        ans = [root.val]
        queue = deque([root])
        while queue:
            size = len(queue)
            heap = []
            for _ in range(size):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                    heappush(heap , -node.right.val)
                if node.left:
                    queue.append(node.left)
                    heappush(heap , -node.left.val)
            if heap:
                val = heappop(heap)
                ans.append(-val)
        
        return ans