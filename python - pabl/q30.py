arr = [1, 6, 2]
n = len(arr)

stack = []
result = []

for i in range(n):
    while stack and stack[-1] >= arr[i]:
        stack.pop()
    
    if not stack:
        result.append(-1)
    else:
        result.append(stack[-1])
    
    stack.append(arr[i])

print(result)
