
def string_reduce(s):
    stack = []

    for i in s:
        if stack:
            char = stack[-1]
            if char.lower()==i.lower():
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    return "".join(stack)

print(string_reduce("aBbA"))
print(string_reduce("abBA"))
print(string_reduce("CabbAac"))
print(string_reduce("Hello World"))
