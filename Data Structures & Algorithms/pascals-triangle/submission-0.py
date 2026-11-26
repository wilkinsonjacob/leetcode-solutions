class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            new_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    new_row.append(1)
                else:
                    value = result[i - 1][j - 1] + result[i - 1][j]
                    new_row.append(value)
            result.append(new_row)
                
        return result