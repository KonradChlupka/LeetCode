class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": 0, "{": 0, "[": 0}
        most_recent = []
        for char in s:
            if char == ")":
                if d["("] == 0 or most_recent[-1] != "(":
                    return False
                else:
                    d["("] -= 1
                    most_recent.pop()
            elif char == "}":
                if d["{"] == 0 or most_recent[-1] != "{":
                    return False
                else:
                    d["{"] -= 1
                    most_recent.pop()
            elif char == "]":
                if d["["] == 0 or most_recent[-1] != "[":
                    return False
                else:
                    d["["] -= 1
                    mot_recent.pop()
            elif char in "({[":
                d[char] += 1
                most_recent.append(char)
        return not any(d.values())
