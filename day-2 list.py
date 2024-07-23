 ''' list is ordered,mutable
 list methods
append--- adding elements in end of list
insert--- particular postion
reverse---reverse
sort---asc,des
copy---same thing
pop---delect in last'''
#my_list=[1,2,9,3,4,2,0,-7,]
#my_list.append(9999)
#print(my_list)
#my_list.insert(1,999)
#print(*my_list)
#print(len(my_list))
#my_list.pop(2)
#my_list2=[5,6,7,8]
#new_list=my_list+my_list2
#new_list=my_list.copy()
#new_list.pop()
#print(*new_list)
#print(*my_list)
#cnt=new_list.count(2)
#print(cnt)
# #my_list.sort()
#pricnt(my_list)
#new_list.sort()
#print(len(new_list))
'''for dynamic list we use my_list=list(map(int,input().split(""))) map for more than 1 ip,int-datatype,split for seprator list is typecast'''
'''a="hello"
for i in range(len(a)):
    print(a[i],end=" ")
print("\n-------------------")
for i in a:
    print(i,end="")'''


'''my_list=list(map(int,input().split()))
for i in  range(len(my_list)):
    print(my_list[i],end="@")
for i in my_list:
    print(i,end=" ")'''


'''list=[]
n=int(input())
for i in range(1,n+1):
    list.append(i)
    print(list)'''


'''my_list=list(map(int,input().split(",")))
#my_list.append(2)
#print(my_list)
print("1.append")
print("2.pop")
print("3.sort")
print("4.length")
print("5.exit")
print("enter your choice")
choice=int(input())
if choice==1:
    my_list.append(9)
    print(*my_list)
elif choice==2:
    my_list.pop(2)
    print(*my_list)
elif choice==3:
    my_list.sort()
    print(*my_list)
elif choice==4:
    print(len(my_list))
else:
    exit()
    print("exit")'''
 
