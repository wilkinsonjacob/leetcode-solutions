class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # prefill result with a list of list 0s [[0], [0], [0]]
        result = [0] * len(temperatures)
        stack = []

        # loop through temperatures and get their index
        for idx, temp in enumerate(temperatures):
            # while stack has something in it and curr temp is greater than the last temp added
            while stack and temp > stack[-1][0]:
                # pop out latest temp and index pair
                stackT, stackInd = stack.pop()
                # append at stack idx from pair the difference of curr index and stack idx of pair
                result[stackInd] = idx - stackInd
            # if stack is empty or curr temp is <= last temp added, append curr pair
            stack.append((temp, idx))
        return result