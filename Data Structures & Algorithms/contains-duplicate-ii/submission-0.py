class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for idx in range(len(nums)):
            if nums[idx] not in seen:
                seen[nums[idx]] = idx
                continue
            
            if abs(idx - seen[nums[idx]]) <= k:
                return True
            else:
                seen[nums[idx]] = idx
        return False
