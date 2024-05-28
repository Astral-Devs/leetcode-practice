def maxProfit(self, prices: List[int]) -> int:
        best = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if profit < prices[i] - best:
                profit = prices[i] - best

            if best > prices[i]:
                best = prices[i]

        return profit
