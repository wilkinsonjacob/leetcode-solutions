class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left_ptr: int = 0
        curr_ptr: int = 0
        right_ptr: int = len(nums) - 1

        while curr_ptr <= right_ptr:
            # [1,0,2]
            if nums[curr_ptr] == 0:
                temp = nums[left_ptr]
                nums[left_ptr] = nums[curr_ptr] # [0, 0, 2]
                nums[curr_ptr] = temp # [0, 1, 2]
                # increment l_ptr and c_ptr
                left_ptr += 1
                curr_ptr += 1
            # [1, 2, 1]
            elif nums[curr_ptr] == 2:
                temp = nums[right_ptr]
                nums[right_ptr] = nums[curr_ptr] # [1, 2, 2]
                nums[curr_ptr] = temp # [1, 1, 2]
                right_ptr -= 1
            else:
                # [0, 1, 2]
                curr_ptr += 1

        