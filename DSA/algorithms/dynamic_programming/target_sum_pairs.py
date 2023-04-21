# Given to arrays get how many pairs of elements (one from each arrays) sums the target

#  Brute force solutions: check every single pair

def get_all_pairs(arr1: list, arr2: list, target) -> int:
    cache: list = []
    
    for i in range(len(arr1)):
        cache.append(target - arr1[i])
        
    n: int = 0
    for i in range(len(arr2)):
        if arr2[i] in cache:
            n += 1
    
    return n


arr1 = [1, 3, 5, 0, 1,]
arr2 = [4, 4, 3, 2, 2,]
target = 3

print(get_all_pairs(arr1, arr2, target))