#pattern for upper triangle
for i in range(5):
    for j in range(5):
        if(i==j or i<j):
            print("*",end="")
    print()    