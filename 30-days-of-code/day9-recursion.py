# Using iterative (for loop)
def loop_factorial(n):
    my_value = 1

    for i in range(1, n):
        my_value *= (i+1)

    return my_value

# Using recursion
def rec_factorial(n):
    if n == 0:
        return 1
    else:
        # Check the value decrementing
        print(f"value of N - {n}")
        return n * rec_factorial(n - 1)

print(f"\nThis is the factorial - {rec_factorial(4)}")