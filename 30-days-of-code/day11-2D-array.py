arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

highest_sum = ""
for v_r in range(len(arr)-2):
    for h_r in range(len(arr[v_r])-2):
        
        # Get sum of first row, first 3 items
        row1 = sum(arr[v_r][h_r: (h_r+3)])

        # Get middle of second row, second 3 items
        row2 = arr[v_r+1][(h_r+1)]

        # Get sum of third row, first 3 items
        row3 = sum(arr[v_r+2][h_r: (h_r+3)])

        # Compute sum of all values from all rows
        hourglass_sum = row1 + row2 + row3

        # Set as highest sum if no values yet
        if highest_sum == "":
            highest_sum = highest_sum = hourglass_sum
        
        # Set as the highest sum if sum is greater than current value
        elif highest_sum < hourglass_sum:
            highest_sum = hourglass_sum
            
        else:
            pass

print(highest_sum)