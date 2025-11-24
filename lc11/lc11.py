def maxWater(arr: list[int]) -> int:
    # iterate from both ends to find the best solution
    i = 0
    j = len(arr) - 1   # last valid index
    best = 0
    curMax = 0

    while i < j:
        curMax = min(arr[i], arr[j]) * (j - i)
        if curMax > best:
            best = curMax
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1

    return best

print(maxWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxWater([1, 1]))
print(maxWater([1, 2, 3, 4, 5, 6, 7, 8]))
print(maxWater([8, 7, 6, 5, 4, 3, 2, 1]))
print(maxWater([1, 3, 7, 9, 7, 3, 1]))


