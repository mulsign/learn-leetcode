def arrangeCoins(n: int) -> int:
        k = 1
        while n > 0:
            n = n - k
            k += 1
        if n < 0:
            return k-2
        else:
            return k-1

print(arrangeCoins(7))