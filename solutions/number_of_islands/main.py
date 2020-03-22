class Solution:
    def dfs(self, r, c):
        self.grid[r][c] = "0"
        if c < self.n_cols - 1 and self.grid[r][c + 1] == "1":
            self.dfs(r, c + 1)
        if c > 0 and self.grid[r][c - 1] == "1":
            self.dfs(r, c - 1)
        if r < self.n_rows - 1 and self.grid[r + 1][c] == "1":
            self.dfs(r + 1, c)
        if r > 0 and self.grid[r - 1][c] == "1":
            self.dfs(r - 1, c)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        self.grid = grid
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == "1":
                    islands += 1
                    self.dfs(r, c)
        return islands
