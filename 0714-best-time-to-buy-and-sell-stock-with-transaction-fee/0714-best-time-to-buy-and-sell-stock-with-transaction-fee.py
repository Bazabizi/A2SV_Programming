class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        profit = [0]*length
        buy = [0]*length
        buy[0] = prices[0]
        
        for idx in range(1 , length):
            profit[idx] = max(profit[idx - 1] , prices[idx] - buy[idx -1] - fee)
            buy[idx] = min(buy[idx - 1] , prices[idx] - profit[idx - 1])
        
        return profit[-1]