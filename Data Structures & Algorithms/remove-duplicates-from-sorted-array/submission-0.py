class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # set first pointer to the second element     
        left_ptr: int = 1

        # set second pointer to the second element and have it loop from there to the last element
        for right_ptr in range(1, len(nums)):
            # if the element at the curr right pointer does not equal the element to its left then it is a unique element
            if nums[right_ptr] != nums[right_ptr - 1]:
                print(nums)
                # we can make the left pointer equal to that unique element
                nums[left_ptr] = nums[right_ptr]
                print(nums)
                # move the left pointer to the next element
                left_ptr += 1
        # return unique elements
        return left_ptr