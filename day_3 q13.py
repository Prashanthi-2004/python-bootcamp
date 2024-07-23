'''replace the elements in an array with the average of maximum and minimum elements
testcase:0
13 2 67 20 68
68+2=70/2==35
35 35 35 35 35 '''
my_list=list(map(int,input().split()))
min_elememt=my_list[0]
max_element=my_list[0]
for i in range(0,len(my_list)):
     if(my_list[i]<min_element):
        min_element=my_list[i]
     if(my_list[i]>max_element):
        max_element=my_list[i]
avg=(max_element+min_element)//2
 for i in range(len(my_list)):
 my_list[i]=avg
print(my_list)            


  