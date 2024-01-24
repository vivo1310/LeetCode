class Solution:
    def fib(self, n: int) -> int:
        f = {}
        f[0] = 0
        f[1] = 1
        if n in f:
            return f[n]
        for i in range(2, n + 1):
            f[i] = f[i-1] + f[i-2]
        return f[n]