class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        size = len(nums)//3
        for key , val in count.items():
            if val > size:
                ans.append(key)
        
        return ans