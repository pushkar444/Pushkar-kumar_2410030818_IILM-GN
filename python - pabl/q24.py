def largest_string_after_k_deletions(s, k):
    stack = []

    for char in s:
        while stack and k > 0 and stack[-1] < char:
            stack.pop()
            k -= 1
        stack.append(char)

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)


# Taking input
s = input("Enter string: ")
k = int(input("Enter k: "))

result = largest_string_after_k_deletions(s, k)
print("Output:", result)
