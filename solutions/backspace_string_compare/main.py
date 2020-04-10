class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = len(S) - 1
        t = len(T) - 1
        skip_s = 0
        skip_t = 0
        while True:
            while s > -1 and (skip_s or S[s] == "#"):
                if S[s] == "#":
                    skip_s += 1
                    s -= 1
                else:
                    skip_s -= 1
                    s -= 1
            while t > -1 and (skip_t or T[t] == "#"):
                if T[t] == "#":
                    skip_t += 1
                    t -= 1
                else:
                    skip_t -= 1
                    t -= 1
            if s > -1 and t > -1:
                if S[s] == T[t]:
                    s -= 1
                    t -= 1
                else:
                    return False
            elif s < 0 and t < 0:
                return True
            elif (s > -1 and S[s] != "#") or (t > -1 and T[t] != "#"):
                return False
