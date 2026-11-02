class Solution:
    def validPalindrome(self, s: str) -> bool:
        formatted_str: str = "".join([char for char in s if char.isalnum()])
        left_ptr: int = 0
        right_ptr: int = len(formatted_str) - 1

        while left_ptr < right_ptr:
            if formatted_str[left_ptr] != formatted_str[right_ptr]:
                # Skip Left
                skip_left = formatted_str[left_ptr + 1:right_ptr + 1]
                # Skip Right
                skip_right = formatted_str[left_ptr:right_ptr]
                # Return whether skip succeeds
                return (skip_left == skip_left[::-1]
                        or skip_right == skip_right[::-1])
            
            left_ptr += 1
            right_ptr -= 1
            
        return True
