class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find dimensions
        n_rows = len(grid)
        n_cols = len(grid[0])

        # find initial rotten oranges
        rottens = []
        for i_row, row in enumerate(grid):
            for i_col, el in enumerate(row):
                if el == 2:
                    rottens.append((i_row, i_col))

        # rot all possible and find number of steps
        steps = -1
        there_was_change = True
        while there_was_change:
            steps += 1
            there_was_change = False
            rottens_copy = rottens[:]
            rottens = []
            for rotten in rottens_copy:
                if rotten[1] < n_cols - 1 and grid[rotten[0]][rotten[1] + 1] == 1:
                    grid[rotten[0]][rotten[1] + 1] = 2
                    rottens.append((rotten[0], rotten[1] + 1))
                    there_was_change = True
                if rotten[0] < n_rows - 1 and grid[rotten[0] + 1][rotten[1]] == 1:
                    grid[rotten[0] + 1][rotten[1]] = 2
                    rottens.append((rotten[0] + 1, rotten[1]))
                    there_was_change = True
                if rotten[1] > 0 and grid[rotten[0]][rotten[1] - 1] == 1:
                    grid[rotten[0]][rotten[1] - 1] = 2
                    rottens.append((rotten[0], rotten[1] - 1))
                    there_was_change = True
                if rotten[0] > 0 and grid[rotten[0] - 1][rotten[1]] == 1:
                    grid[rotten[0] - 1][rotten[1]] = 2
                    rottens.append((rotten[0] - 1, rotten[1]))
                    there_was_change = True

        # see if there are any unreachable left
        for row in grid:
            for el in row:
                if el == 1:
                    return -1

        return steps
