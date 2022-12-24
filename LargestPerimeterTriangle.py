class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter=0
        length=len(nums)
        first=length-1
        second=length-2
        third =length-3

        while length>2:
            if nums[first] < nums[second] + nums[third]:
                perimeter = nums[first] + nums[second] + nums[third]
                return perimeter
            
            first-=1
            second-=1
            third-=1
            length-=1

        return 0
