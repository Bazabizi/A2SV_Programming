class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        total = 0
        first = skill[0]
        last = skill[-1]
        sums = first + last
        
        while left < right:
            if skill[right] + skill[left] != sums:
                return -1
            total += skill[right] * skill[left]
            left += 1
            right -=1
        
        return total