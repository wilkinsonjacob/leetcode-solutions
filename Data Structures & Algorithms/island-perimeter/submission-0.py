class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        perimeter: int = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                perimeter += 4

                if row + 1 < rows and grid[row + 1][col] == 1:
                    perimeter -= 2
                
                if col + 1 < cols and grid[row][col + 1] == 1:
                    perimeter -= 2
        
        return perimeter