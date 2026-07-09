# Trapping Rain Water

class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        leftMax = rightMax = 0
        water = 0

        while left < right:
            if arr[left] <= arr[right]:
                if arr[left] >= leftMax:
                    leftMax = arr[left]
                else:
                    water += leftMax - arr[left]
                left += 1
            else:
                if arr[right] >= rightMax:
                    rightMax = arr[right]
                else:
                    water += rightMax - arr[right]
                right -= 1

        return water
