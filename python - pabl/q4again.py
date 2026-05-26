class Solution:
    def findUnion(self, a, b):
        union_set = set(a + b)
        return list(union_set)

a = [1, 2, 3]
b = [3, 4, 5]

obj = Solution()
print(obj.findUnion(a, b))