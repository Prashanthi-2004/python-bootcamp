#patterns
#square
#*****
#*****
#*****
#*****
#*****
#outer loop print row
#inner loop print column
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()'''
#another pattern
for i in range(10):
    for j in range(10):
        if(i==j):
          print(" ",end="")
        else:
          print("*",end="")
    print()

