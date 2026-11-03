class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for op in operations:
            if op == "+":
                nums.append(nums[-1] + nums[-2])
            elif op == "C":
                nums.pop()
            elif op == "D":
                nums.append(nums[-1] * 2)
            else:
                nums.append(int(op))
        return sum(nums)