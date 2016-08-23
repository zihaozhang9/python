#折半二分查询算法
def BinarySearch(a, target): 
    low = 0
    high = len(a) - 1
 
    while low <= high:
 
        mid = (low + high) // 2
        midVal = a[mid]
 
        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return mid
    return -1