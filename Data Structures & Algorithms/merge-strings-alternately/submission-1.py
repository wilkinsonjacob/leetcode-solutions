class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res: str = ""
        ptr: int = 0

        word1_length: int = len(word1)
        word2_length: int = len(word2)
        length: str = max(word1_length, word2_length)

        while ptr < length:
            if ptr < word1_length:
                res += word1[ptr]
            if ptr < word2_length:
                res += word2[ptr]
            ptr += 1

        return res
