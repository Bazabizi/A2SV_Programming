class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        size1 = len(players)
        size2 = len(trainers)
        ans = 0
        idx1 = 0
        idx2 = 0
        
        while idx1< size1 and idx2 < size2:
            if trainers[idx2]>= players[idx1]:
                ans += 1
                idx2+= 1
                idx1 += 1
            else:
                idx2 +=1
        
        return ans
                