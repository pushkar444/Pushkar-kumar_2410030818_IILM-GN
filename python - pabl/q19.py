class Solution:
    def spirallyTraverse(self, mat):

        result = []

        top = 0
        bottom = len(mat) - 1

        left = 0
        right = len(mat[0]) - 1

        while top <= bottom and left <= right:

            # Left to Right
            for i in range(left, right + 1):
                result.append(mat[top][i])

            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])

            right -= 1

            # Right to Left
            if top <= bottom:

                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])

                bottom -= 1

            # Bottom to Top
            if left <= right:

                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])

                left += 1

        return result
       
            