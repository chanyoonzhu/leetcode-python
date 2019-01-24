def maxShippingDist(list1, list2, target):

    #edge cases
    if not list1 or not list1[0] or not list2 or not list2[0]: 
        return []
    
    res = []
    largestDist = 0
    for item1 in list1:
        for item2 in list2:
            if len(item1) == 2 and len(item2) == 2: 
                if item1[1] + item2[1] <= target:
                    largestDist = max(largestDist, item1[1] + item2[1])
    for item1 in list1:
        for item2 in list2:
            if len(item1) == 2 and len(item2) == 2:
                if item1[1] + item2[1] == largestDist:
                    res.append([item1[0], item2[0]])
    return res

list1 = [[1,3000], [2, 5000], [3, 7000], [4, 10000]]
list2 = [[1,2000], [2, 3000], [3, 4000], [4, 5000]]
target = 10000
print(maxShippingDist(list1, list2, target))
