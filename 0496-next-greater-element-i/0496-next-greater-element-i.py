class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterElement = defaultdict(lambda:-1)
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                greaterElement[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = []
        
        for num in nums1:
            ans.append(greaterElement[num])
        return ans 
            
                