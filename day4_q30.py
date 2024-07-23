#password verifier
#mr x is trying to create a new password for his insta account these are the required conditions
#for creating a new password
#condtn-1 min length is 8 and max len is 15
#condtn-2 only @,\ are allowed in password
#condtn-3 no spaces are allowed
#condtn-4 only alphanumerics are allowed
#you are suppose to print weak if length is exact 8,
#medium if length is b/w 8-12
#strong if length is b/w 12-15'''
pw=input()
str='@,\'
cnt=0
for i in @:
if((len(pw)<8)):
    print("follow the below conditions")
elif(len(pw)==8):
    print("weak")
elif((len(pw)>8) and (len(pw)<12)):
    print("medium")
elif((len(pw)>12) and (len(pw)<15)):
    print("strong")
else:
    print("invalid")