class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for num in range(n + 1):
            val = 1
            for _ in range(17):
                if num & val:
                    ans[-1] += 1
                val = val << 1
                if val > num:
                    break
            ans.append(0)
        ans.pop()
        return ans