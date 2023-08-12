class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        k = (-1 +math.sqrt(1 + 8*len(grades)))//2
        return int(k)