def fibonacci(position):
    if position < 2:
        return position
    else:
        return(fibonacci(position-1) + fibonacci(position-2))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))