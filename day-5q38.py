#write a code to print all the capital letters in given string
str=input()
ans=""
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        ans+=i
print(ans)             