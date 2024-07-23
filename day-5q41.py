#ENCODING DECODING QUESTION
#if the input is given as XYZ then it should print ABC because after XYZ no numbers so cyclic format ABC we should print************
#XYZ
#x=120+3=123-26----->97=a
#chr(123)  |
#y=121+3=124-26----->98=b
#chr(124)   }
#z=122+3=125-26----->99=c
#chr(125)    ~
#relation is 26 so we should subtract with 26
str="XYZ"
for i in str:
    print(chr((ord(i)+3)-26),end="")
      