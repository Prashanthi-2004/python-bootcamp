#print all the vowels followed by consonents
vowels="aeiou"
cons="bcdfghjklmnpqrstuvwxyz"
ans=""
i="amazing"
inp=i.lower()
for i in inp:
    if( i in vowels):
        ans+=i
for i in inp:
    if(i in cons):
        ans+=i
print(ans)                      
    
        
        
