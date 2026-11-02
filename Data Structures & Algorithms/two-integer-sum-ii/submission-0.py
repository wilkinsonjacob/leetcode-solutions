class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for idx, num in enumerate(numbers):
            if num not in seen:
                seen[target - num] = idx + 1
                continue
            return [seen[num], idx + 1]