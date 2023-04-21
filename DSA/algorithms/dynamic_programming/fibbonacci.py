from typing import Callable
from performance import timer


# Time Complexity: O(n) -> Space Complexity: O(n)
def fibonacci_memoized() -> Callable:
    cache: dict = {}
    
    def fib_mem(n) -> int:
        if n in cache: return cache[n]
        if n < 2:  return n
        cache[n] = fib_mem(n - 1) + fib_mem(n - 2)
        return cache[n]

    return fib_mem


def fibonacci_table(n: int) -> int:
    cache = []
    
    if n < 2:
        return n
    
    cache.append(0)
    cache.append(1)
    
    for i in range(2, n + 1):
        cache.append(cache[i - 1] + cache[i - 2]) 
    
    return cache.pop()
    

if __name__ == "__main__":
    with timer("fibonacci memoized"):
        fib_memo = fibonacci_memoized() 
        print([fib_memo(n) for n in range(20)])
        
    with timer("fibonacci table"):
        print([fibonacci_table(n) for n in range(20)])