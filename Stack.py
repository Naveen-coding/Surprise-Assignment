no_of_elements=int(input())
operations_stack=[]
for i in range(no_of_elements):        
    operation=input()
    operations_stack.append(operation)
stack=[]
for operation in operations_stack:
    if "push" in operation:
        stack.append(int(operation[5:]))
    if operation=="pop":
        stack.pop()
    if operation=="max":
        print(max(stack))
