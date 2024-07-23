'''reverse of a number------>imp prblm
123
321
123%10=3
*****
12%10=2
*****
1%10=1
*****
0'''
n=123
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))    



