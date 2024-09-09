"""
i historically blunder binary search at critical moments due to very small implementation errors
idk how this algorithm is so easy but whatever
"""


# returns index of target
def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        num = nums[mid]
        if num < target:
            low = mid + 1
        elif num > target:
            high = mid - 1
        else:
            return mid
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 999], 999))
