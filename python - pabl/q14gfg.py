class Solution:
    def getMinDiff(self, arr, k):

        n = len(arr)

        if n == 1:
            return 0

        arr.sort()

        ans = arr[n - 1] - arr[0]

        for i in range(n - 1):

            if arr[i + 1] < k:
                continue

            minimum = min(arr[0] + k, arr[i + 1] - k)
            maximum = max(arr[i] + k, arr[n - 1] - k)

            ans = min(ans, maximum - minimum)

        return ans