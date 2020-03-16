class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif char == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif char == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            elif char in "({[":
                stack.append(char)
        print(stack)
        return not stack
