class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        
        # create a list of lists of size nums
        # the count of a number can be at most the length of nums
        freq = [[] for i in range(len(nums) + 1)]

        # count how many times each number appears
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # put a number in the list at index of how many times it appears
        for num, count in count.items():
            freq[count].append(num)

        res = []
        # loop through the list backwards
        for i in range(len(freq) - 1, 0, -1):
            # loop through the nums in the nested list
            for num in freq[i]:
                # append the num
                res.append(num)
                # if the len of res == k return
                if len(res) == k:
                    return res