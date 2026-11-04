class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # case: one index [no selling]
        if (len(prices) == 1):
            return 0
        
        # define: sliding window ptrs
        left, right = 0, 1

        while (right < len(prices)):
            # case: left pointer moves
            if prices[left] > prices[right]:
                left = right 
                right += 1
                continue
            
            # case: calculate profit 
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            right += 1
            

        return max_profit