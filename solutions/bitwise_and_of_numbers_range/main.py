class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        for i in range(32):
            if m == n:
                break
            m >>= 1
            n >>= 1
        return m << i
