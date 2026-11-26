class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                curr_count = 0
            max_ones = max(curr_count, max_ones)
        
        return max_ones