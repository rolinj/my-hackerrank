input_count = int(input())
for _ in range(input_count):
    input_string = input()
    odd = ""
    even = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            even += input_string[i]
        else:
            odd += input_string[i]
        
    print(even + " " + odd)