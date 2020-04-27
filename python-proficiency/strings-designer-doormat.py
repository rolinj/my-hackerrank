# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = input().split()
width = int(x)
height = int(y)
char_fill = ".|."

half_width = width//2
half_height = (height - 3)//2

#TOP SECTION
for i in range(half_width):
    print((char_fill * i).rjust(half_height, "-") + char_fill + (char_fill * i).ljust(half_height, "-"))

#CENTER LINE
print(("WELCOME").center(height, "-"))

#BOTTOM SECTION
for i in range(1, half_width + 1):
    print((char_fill * (half_width - i)).rjust(half_height, "-") + char_fill + (char_fill * (half_width - i)).ljust(half_height, "-"))

