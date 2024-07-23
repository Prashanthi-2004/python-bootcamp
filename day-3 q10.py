'''print the element present in k index
k=3
3 6 8 4 61 2
o/p:4'''
'''k=8
80 70 54 36 72
o/p:36'''
'''k=20
70 54 36 72 76 9999 0089
1 2 3 4 5 6 7-->indx
k=20,7
indx=6'''
'''k=18
80 70 54 36 77
1 2 3 4 5-->indx
k=18,5
indx=3''' 
'''k=38
70 54 36 72 566
1 2 3 4 5
k=38,5
indx=3'''
my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])




