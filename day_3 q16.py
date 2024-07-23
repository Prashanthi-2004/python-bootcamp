'''sum of  digits
123%10=3
3
123/10=12
n=12
12%10=2
3+2=5
12/10=1
n=1
1%10=1
5+1=6
1/10=0'''
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r#----->imp line
    n=n//10
print(sum) 
#r means remainder   