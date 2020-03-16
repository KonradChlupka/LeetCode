class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in parentheses_map:
                if len(stack) == 0 or stack.pop() != parentheses_map[char]:
                    return False
            elif char in "({[":
                stack.append(char)
        return not stack
