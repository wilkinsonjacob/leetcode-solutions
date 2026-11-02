class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str: str = "".join([char for char in s if char.isalnum()]).lower()
        str_len = len(formatted_str)
        left_ptr: int = 0
        right_ptr: int = str_len - 1

        while left_ptr < (str_len // 2):
            if formatted_str[left_ptr] != formatted_str[right_ptr]:
                return False
            
            left_ptr += 1
            right_ptr -= 1
        
        return True
        