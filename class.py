class myclass:     #create a class 
    x = 5
obj = myclass()                #create  an class object
print(obj.x)


print("________________________________")
#create class 
class person:
    def __init__(self,name,age):      #name and age local veriable
        self.name = name       #instence veriable
        self.age = age
#create a class obj
obj = person("attu",18)

print(obj.name)         #call class
print(obj.age)