'''find the duplicates in an array
8 7 7 8 5 4 4 8 9
8 7 4'''
l=list(map(int,input().split()))
for i in l:
    if(i in [l]):
        [].appends(i)
print([l])