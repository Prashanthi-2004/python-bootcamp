#input is given as hello-------wo------- rld
#output format as -----------hello world
str=input()
cnt=0
ans=""
for i in str:
    if(i=="-"):
        cnt+=1
    else:
        ans=ans+i
print("-"*cnt+ans)        

    


