# S = input().strip()

# try:
#     print(int(S))
# except:
#   print("Bad String")

import string
alphabet = list(string.ascii_lowercase)

def print_rangoli(size):
    # your code goes here

    # top section


    # middle section
    for i in range(size-1):
        print(alphabet[size-(i+1)] , end = "-")
    
    # bottom section

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)