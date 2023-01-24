class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        ans=[]
        while left <= right:
            num = numbers[right] + numbers[left]
            if num < target:
                left += 1
            elif num > target:
                right -= 1
            else:
                ans.append(left+1)
                ans.append(right+1)
                break
        return ans