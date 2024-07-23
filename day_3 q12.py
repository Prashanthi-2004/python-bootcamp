#find the minimum element in the given list
my_list=list(map(int,input().split()))
minimum=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]<minimum):
        minimum=my_list[i]
print(minimum)
