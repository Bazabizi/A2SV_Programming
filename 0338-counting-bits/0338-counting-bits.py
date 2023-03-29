class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for num in range(n + 1):
            for _ in range(17):
                if num & 1:
                    ans[-1] += 1
                num = num >> 1
            ans.append(0)
        ans.pop()
        return ans