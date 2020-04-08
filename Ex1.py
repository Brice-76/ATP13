class Node :
    def __init__(self,val,right=False,left=False):
        self.__val=val
        self.__right=right
        self.__left=left

    def get_val(self):
        return self.__val
    def get_right(self):
        return self.__right
    def get_left(self):
        return self.__left
    def set_val(self,val):
        self.__val=val
    def set_right(self,right):
        self.__right=right
    def set_left(self,left):
        self.__left=left

n1=Node(3)
n2=Node(4,False,n1)
n3=Node(6)
n4=Node(5,n3,n2)
n5=Node(18)
n6=Node(21)
n7=Node(19,n6,n5)
n8=Node(17,n7)
nfin=Node(12,n8,n4)



