stack = []

#push
stack.append('A')
stack.append('B')
stack.append('C')
print(stack)

#peek to see an element in the satck 
top_element = stack[-1]
print(f"top element : {top_element}")

# pop remove the last elemnt or top element
popped_element = stack.pop()
print(f"{popped_element} is popped form the stack")
print(f"Current stack elements are : {stack}")