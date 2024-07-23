#check how many vowels in a string
'''str=input()
cnt=0
v=['a','e','i','o','u']
for i in str:
    if i in v:
        cnt+=1
print(cnt) '''
#to convert lower to upper
'''check=['a','e','i','o','u']
cnt=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if (i in check):
        cnt+=1
print(cnt) '''  

#consonants count
'''str=input()
cnt=0
v=['a','e','i','o','u']
for i in str:
    if i not in v:
        cnt+=1
print(cnt)''' 
#we use len for space
#we can use list for input in str
vowel="aeiou"
cons="bcdfghjklmnpqrstvwxyz"
cnt=0
cons=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if (i in vowel):
        cnt+=1
for i in inp:
    if i not in vowel:
        cnt+=1        
print(cnt,cons) 


    