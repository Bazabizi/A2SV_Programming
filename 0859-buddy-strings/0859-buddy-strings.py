class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        scount = Counter(s)
        goalCount = Counter(goal)
        if scount == goalCount and max(scount.values()):
            count = 0
            for sval , gval in zip(s , goal):
                if sval != gval:
                    count += 1
            if count == 0 and max(scount.values()) > 1 :
                return True
        
            if count == 2:
                return True
        return False
    