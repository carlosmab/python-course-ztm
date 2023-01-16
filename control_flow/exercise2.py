# find duplicates

some_list = ['a', 'a', 'd', 'e', 'd', 'm', 'n', 'm', 'n']

duplicates = []
for i, x in enumerate(some_list):
    for j, y in enumerate(some_list):
        if i == j: continue
        if x == y:
            if x not in duplicates:
                duplicates.append(x)
    
print(duplicates)

dict = {}
duplicates = []
for x in some_list:
    if x not in dict:
        dict[x] = True
    else:
        duplicates.append(x)

print(duplicates)       


duplicates = []
for x in some_list:
    if some_list.count(x) > 1:
        if x not in duplicates:
            duplicates.append(x)
print(duplicates)