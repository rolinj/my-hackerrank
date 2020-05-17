import string
alphabet = list(string.ascii_lowercase)

def print_rangoli(size):
    # your code goes here
    if size == 1:
        return print("a")
    
    # top section  ====================================
    print(alphabet[size-1].center((size * 4) - 3, '-'))
    
    for i in range(1, size-1):
        top_list = []
        for x in range(i+1):
            top_list.append(alphabet[(size-(i+1))+x])

        mirror = top_list[::-1][:len(top_list)-1]
        final_list = mirror + top_list

        print("-".join(final_list).center((size * 4) - 3, '-'))

    # middle section  ================================
    mid_list = []
    for i in range(size-1):
        mid_list.append(alphabet[size-(i+1)])

    middle_list = mid_list + ['a'] + mid_list[::-1]
    print("-".join(middle_list))
    

    # bottom section  ================================
    for i in range(1, n-1):
        top_list = []
        for x in range(n-i):
            top_list.append(alphabet[i+x])
        
        mirror = top_list[::-1][:len(top_list)-1]
        final_list = mirror + top_list

        print("-".join(final_list).center((size * 4) - 3, '-'))

    print(alphabet[size-1].center((size * 4) - 3, '-'))

if __name__ == '__main__':
    n = 10
    print_rangoli(n)