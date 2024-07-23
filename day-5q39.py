#remove all the braces from the given algebraic expression
  # [(a+b)+c]
#a+b+c {--123   }==125
#(41              )40
#[91           ] 93 
exp=input()
for i in exp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
print()        