def productExceptSelf(nums: list[int]) -> list[int]:
    if len(nums) == 1: return nums
    if len(nums) == 2: return nums[::-1]
    
    left_products = []
    right_products = []
    products = []
    
    for i, num in enumerate(nums):
        print(i)
        if i == 0: 
            left_products.append(num)
        else:
            left_products.append(left_products[i-1] * num)
    print(left_products)

    for i, num in enumerate(nums[::-1]):
        if i == 0: right_products.append(num)
        else: right_products.append(right_products[i-1] * num)
    print(right_products)

    for i, n in enumerate(nums):
        if i == 0: products.append(right_products[-2])
        elif i == len(nums) - 1: products.append(left_products[i - 1])
        else: products.append(left_products[i - 1] * right_products[- i - 2])
    
    return products   

print(productExceptSelf([1,2,3,4]))

#  _ * 24 = 24
#  1 * 12 = 12
#  2 * 4 = 8
#  6 * _ = 6