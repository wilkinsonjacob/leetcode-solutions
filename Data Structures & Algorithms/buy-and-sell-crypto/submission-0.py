class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr: int = 0
        r_ptr: int = 1
        max_prof: int = 0

        while r_ptr < len(prices):
            # if todays buy price > future sell price: not profitable
            if prices[l_ptr] > prices[r_ptr]:
                l_ptr = r_ptr
                r_ptr += 1
                continue
            # if todays buy price < future sell price: profitable
            max_prof = max(max_prof, prices[r_ptr] - prices[l_ptr])
            r_ptr += 1
        return max_prof