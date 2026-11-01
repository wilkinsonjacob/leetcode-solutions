class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        curr = 1
        while curr in nums_set:
            curr += 1
        return curr