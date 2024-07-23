#input is given as hello123
#output is 6
#sum is sum of digits
'''str="hello123"
d="0123456789"
sum=0
for i in str:
    if i in d:
        sum+=int(i)
print(sum)''' 
#sum of digits of a number using ascii values
'''inp=input()
sum=0
for i in inp:
    if(ord(i)>48 and ord(i)<57):
        sum+=int(i)
print(sum)'''   
#to find lowercase letters
'''inp=input()
sum=0
for i in inp:
    if(ord(i)>97 and ord(i)<122):
        sum+=1
print(sum)'''
#to find uppercase letters
inp=input()
sum=0
for i in inp:
    if(ord(i)>65 and ord(i)<90):
        sum+=1
print(sum)                        