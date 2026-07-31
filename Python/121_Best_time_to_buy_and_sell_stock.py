class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for pointer in prices:
            if pointer < min_price:
                min_price = pointer
            else:
                diff = pointer - min_price
                if diff > max_profit:
                    max_profit = diff
        return max_profit