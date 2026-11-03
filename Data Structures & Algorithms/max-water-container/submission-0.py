class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(heights) - 1
        largest = 0

        while l_ptr < r_ptr:
            curr_size = (r_ptr - l_ptr) * min(heights[l_ptr], heights[r_ptr])
            largest = max(curr_size, largest)
            if heights[l_ptr] > heights[r_ptr]:
                r_ptr -= 1
            else:
                l_ptr += 1

        return largest