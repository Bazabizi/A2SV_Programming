class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_l = [0]
        max_r = [0]*(len(height))
        max_r[-1] = len(height) - 1
        if len(height) < 3:
            return 0
        
        for idx in range(1, len(height)):
            index = max_l[-1]
            val = height[max_l[-1]]
            if val <= height[idx]:
                max_l.append(idx)
            else:
                max_l.append(index)
        
        for idx in range(len(height)-2, -1,-1):
            index = max_r[ idx +1 ]
            
            val = height[index]
            if val <= height[idx]:
                max_r[idx] = idx
            else:
                max_r[idx] = index
        
        ans = 0
        
        for idx in range(1 , len(height)-1):
            val1 = height[max_l[idx]]
            val2 = height[max_r[idx]]
            difference = min(val1 , val2) - height[idx] 
            ans += difference if difference > 0 else 0
            
        return ans