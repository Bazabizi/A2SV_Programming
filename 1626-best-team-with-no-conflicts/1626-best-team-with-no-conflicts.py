class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        def valid(score1  , score2):
            if score1[0] == score2[0]:
                return True
            if score1[1] > score2[1]:
                return False
            return True
        
        length = len(scores)
        dp = [0]*length
        ageScore = []
        for age , score in zip(ages, scores):
            ageScore.append([age,score])
        
        ageScore.sort()
        
        for idx in range(length-1 , -1 , -1):
            count = 0
            for idx2 in range(idx , length):
                if valid(ageScore[idx] , ageScore[idx2]):
                    count = max(count , dp[idx2])
            
            dp[idx] = count + ageScore[idx][1]
            
       
        return max(dp)
            