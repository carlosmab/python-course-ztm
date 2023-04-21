# Count how many different ways we can sum (algebraic) the numbers of different
# and array to reach the given target

# Brute force Solution
# 0  1  2  3  4 
# 1  1  1  1  1

# (0, 0)
#                     +1       -1
                    
#                   1, 1      1, -1 

#              2,2      2,0     2,1   2, -2
#  O(2^n)

from typing import Callable


def target_sum(nums: list, target: int) -> int:
    cache = {} # (index, total)
    
    def caching(i, total) -> int:
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in cache:
            return cache[(i, total)]
        
        cache[(i, total)] = ( caching(i + 1, total + nums[i]) + caching(i + 1, total - nums[i]) )
    
        return cache[(i, total)]
    
    return caching(0, 0)
    
print(target_sum([1,1,1,1,1],3))