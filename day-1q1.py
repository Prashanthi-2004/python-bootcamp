#take an input from user
#+ve,even,+veodd
#-ve even
#-ve odd
n=int(input())
if n%2==0 and n>0:
    print("postive even")
elif n%2==0 and n<0:
    print("negative even")
elif n<0:
    print("negative odd")
else:
    print("postive odd")