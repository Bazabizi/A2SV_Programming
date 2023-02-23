class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        left = 0 
        ans = 1 
        up = False
        down = False
        for right in range(1,length):
            if arr[right] < arr[right -1]:
                if down:
                    left = right-1
                down = True
                up = False
            elif arr[right] > arr[right -1]:
                if up:
                    left = right-1
                up= True
                down = False
            else:
                left = right
            # print(left , right)
            ans = max(ans,right - left + 1)
        return ans