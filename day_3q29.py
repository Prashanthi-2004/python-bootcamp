#******find the peak element in the array
'''my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):
    if(my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]):
        cnt+=1
        break
print(my_list[cnt])'''
#to print all the peak elements
'''my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):
    if(my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]):
        print(my_list[i],end=" ")'''      
#if the list is in sorted order then the peak element is last one    
my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):
    if(my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]):
        count+=1
if(my_list[-1]>my_list[-2] and my_list[-1]>cnt):
    cnt=len(my_list)-1
print(my_list[cnt])  