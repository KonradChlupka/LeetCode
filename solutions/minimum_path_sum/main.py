class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        shortest = [0] + [float("inf")] * (cols - 1)
        for i_row in range(rows):
            shortest[0] = shortest[0] + grid[i_row][0]
            for i_col in range(1, cols):
                shortest[i_col] = grid[i_row][i_col] + min(
                    shortest[i_col - 1], shortest[i_col]
                )
        return shortest[-1]
