class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        ans: list[int] = []

        for idx, num in enumerate(nums):
            diff: int = target - num
            if num in seen.keys():
                return [seen[num], idx]
            seen[diff] = idx
