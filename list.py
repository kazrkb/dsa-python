my_array = [7,2,3,10,50]
min_val = my_array[0]

for num in my_array:
    if num < min_val:
        min_val = num
print(f"loswest value is : {min_val}")