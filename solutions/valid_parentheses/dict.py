class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": 0, "{": 0, "[": 0}
        most_recent = []
        parentheses_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in parentheses_map:
                if d[parentheses_map[char]] == 0 or most_recent[-1] != parentheses_map[char]:
                    return False
                else:
                    d[parentheses_map[char]] -= 1
                    most_recent.pop()
            elif char in "({[":
                d[char] += 1
                most_recent.append(char)
        return not any(d.values())
