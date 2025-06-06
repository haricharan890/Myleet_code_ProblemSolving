class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Assume we buy on the first day
        buy = prices[0]

        # No profit made yet
        profit = 0

        # Check every price from the second day onward
        for price in prices[1:]:
            # If current price is cheaper, update the best buy price
            if price < buy:
                buy = price
            # Else, see if selling now gives more profit
            elif price - buy > profit:
                profit = price - buy

        # Return the highest profit we could make
        return profit