def minimize_heights(arr, k):
    n = len(arr)
    arr.sort()
    
    ans = arr[n-1] - arr[0]
    
    for i in range(n - 1):
        if arr[i+1] - k < 0:
            continue
        
        minimum = min(arr[0] + k, arr[i+1] - k)
        maximum = max(arr[i] + k, arr[n-1] - k)
        
        ans = min(ans, maximum - minimum)
    
    return ans

arr = [1, 5, 8, 10]
k = 2

print("Minimum difference:", minimize_heights(arr, k))