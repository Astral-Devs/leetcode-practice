def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_stock = prices[0]

        for i in range(0,len(prices)):
            if prices[i] > current_stock:
                profit += prices[i] - current_stock
            current_stock = prices[i]

        return profit
