# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(n):
    if n == 1:
        return False
    else:
        # Transpose to int to ensure whole number result
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0 and i != n:
                return False
        return True


t = int(input())
my_list = []
for _ in range(t):
    n = int(input())
    my_list.append(n)

for i in range(len(my_list)):

    if is_prime(my_list[i]):
        print("Prime")
    else:
        print("Not prime")