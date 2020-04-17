class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = 0
        open_max = 0
        for c in s:
            if c == "(":
                open_min += 1
                open_max += 1
            elif c == ")":
                open_min -= 1
                open_max -= 1
            else:
                open_min -= 1
                open_max += 1
            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0
        return open_min == 0
