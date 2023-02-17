from abc import ABC , abstractmethod

class parent(ABC):
    #common function
    def common_fn(self):
        print("in the common method of parent")
    @abstractmethod
    def abs_fn(self):#is supposed to have different implementation in child classes
        pass
class child1(parent):
    def abs_fn(self):
        print("in the abstract method of child")   

class child2(parent):
    def abc_fn(self):
        print("In the abstract method of child2")              

obj = child2
obj1 =child1
obj.abc_fn(2)
obj1.abs_fn(4)
obj.common_fn(5)