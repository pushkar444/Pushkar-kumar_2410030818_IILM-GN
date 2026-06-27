def can_place(arr, k, dist):
    count = 1
    last = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]
            if count == k:
                return True
    return False


def max_min_diff(arr, k):
    arr.sort()
    low = 0
    high = arr[-1] - arr[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(arr, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


# Given input in code
arr = [2, 6, 2, 5]
k = 3

result = max_min_diff(arr, k)
print(result)