class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        cur = 1
        for num in target:
            print(num)
            diff = num - cur
            if num != cur:
                ans.extend( ['Push' , 'Pop']*diff)
            ans.append('Push')
            cur = num + 1    
        return ans
