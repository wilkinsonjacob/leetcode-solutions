class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        rows: int = len(grid)
        cols: int = len(grid[0])
        islands: int = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    islands += 1


        return islands

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:

        if (i < 0 
            or i >= len(grid) 
            or j < 0 
            or j >= len(grid[0]) 
            or grid[i][j] != "1"):
            return

        grid[i][j] = "0"

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
