#multiple inheritance
class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class" 
class kid(Father,Mother):
    def kid_speak():
        return "im kid,im having properties of my father and mother" 
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())   
print(obj1.kid_speak())    