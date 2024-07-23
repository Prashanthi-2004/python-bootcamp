'''find the element that is present in K+N index
K=3
N=2
3 6 8 4 61 2
OP:2'''
'''K=3
N=4
80 70 54 36 72'''
my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
length=0
if(len(my_list)<(k+n)):
    print("error")
else:
    for i in range(len(my_list)):
        print(my_list[k+n],end=" ")
        break

    


