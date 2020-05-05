entry_count = int(input())

my_dict = {}
for _ in range(entry_count):
    key, value = input().split()
    my_dict[key] = value

while(True):
    try:
        query_name = str(input())
        if query_name in my_dict:
            print(f"{query_name}={my_dict[query_name]}")
        else:
            print("Not found")
    except:
        break