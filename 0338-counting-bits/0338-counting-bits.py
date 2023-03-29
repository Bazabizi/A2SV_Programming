class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            count = 0
            val = num
            for _ in range(20):
                if val & 1:
                    count += 1
                val = val >> 1
            ans.append(count)
        return ans