class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str: str = "".join([char for char in s if char.isalnum()]).lower()
        reversed_str: str = ""

        for i in range(len(formatted_str) - 1, -1, -1):
            reversed_str += formatted_str[i]
        
        if reversed_str != formatted_str:
            return False

        return True
        