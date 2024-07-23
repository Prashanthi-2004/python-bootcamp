'''find the maximum element in given list
test case:0
12 23 36 44 45 57
o/p:57'''
'''test case:1
56 78 -8 12 34 -99
o/p:78'''
my_list=list(map(int,input().split()))
largest_num=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]>largest_num):
        large_num=my_list[i]
print(large_num)



