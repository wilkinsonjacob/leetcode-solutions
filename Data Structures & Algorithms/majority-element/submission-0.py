class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate: int = nums[0]
        count: int = 0
        
        # loop through numbers in nums
        for num in nums:
            # if the count is 0 make the candidate the current num
            if count == 0:
                candidate = num
            # if count != 0 then add 1 to the count if the current num is the candidate. if not -1 from the count 
            count += 1 if num == candidate else -1
            
        return candidate