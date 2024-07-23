'''find the missing number in array
1 2 3 4 5 6 7 8 9 10===55
1 2 3 4 5 7 8 9 10==49
6'''
my_list=list(map(int,input().split()))
n=len(a)+1
k=sum(a)
sum=n*(n+1)//2
print(sum-k)
    