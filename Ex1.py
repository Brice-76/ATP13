class Node :
    def __init__(self,val,right=None,left=None):
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
    def gauche_droite(self):
        return self.__right,self.left
    def __str__(self):
        return 'node val : '+str(self.get_val())


if __name__ == '__main__' :
    n1=Node(1)
    n2=Node(2,n1)
    n3=Node(3,n1,n2)
    print(n3)



