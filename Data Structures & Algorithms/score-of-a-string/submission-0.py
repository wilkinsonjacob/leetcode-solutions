class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        left, right = 0, 1

        while right < len(s):
            ascii_left, ascii_right = ord(s[left]), ord(s[right])
            res += max(ascii_left, ascii_right) - min(ascii_left, ascii_right)
            left += 1
            right += 1
        
        return res
