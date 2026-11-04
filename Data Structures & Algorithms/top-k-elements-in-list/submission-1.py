class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the amount each number appears
        count = collections.Counter(nums)

        # create an empty list
        arr = []
        # loop through the dict and append [count, num] into it
        for num, count in count.items():
            arr.append([count, num])
        # sort the resulting array
        arr.sort()

        res = []
        # check if the len of result is less than k
        while len(res) < k:
            # if it is then append the last elements num to it
            res.append(arr.pop()[1])
        return res