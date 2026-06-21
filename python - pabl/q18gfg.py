class Solution:
    def median(self, mat):

        arr = []

        for row in mat:
            arr.extend(row)

        arr.sort()

        n = len(arr)

        return arr[n // 2]
        
    	