def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

num = int(input("Enter a number: "))
sequence = fibonacci(num)
print("Fibonacci Sequence:")
for number in sequence:
    print(number)
