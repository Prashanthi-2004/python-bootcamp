#input is given as ABC skip value is 4 so
#after A 4values if we skip then E same as for BC
#so output is EFG
str="ABC"
for i in str:
    print(chr(ord(i)+4),end="")
print()