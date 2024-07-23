#find second largest minimum element in array
arr=[12,21,31]
num=0
max1_val=arr[1]
max2_val=arr[1]
for i in arr:
    if num<max1_val:
        max2_val=max1_val
        max1_val=num
    elif num>max2_val:
        max2_val=num
print(max2_val)

