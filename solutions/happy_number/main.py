class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while True:
            if n == 1:
                return True
            if n in history:
                return False
            history.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
