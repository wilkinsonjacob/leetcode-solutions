class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""

        # loop through the smallest word
        for i in range(len(min(strs))):
            # loop through all the words in the list of strs
            for s in strs:
                # for each char in curr string of loop check if it equals the char at the same index of the first str in the list of strs
                if s[i] != strs[0][i]:
                    # if it doesnt return the result
                    return res
            # if it does append that letter to result
            res += strs[0][i]
        
        return res