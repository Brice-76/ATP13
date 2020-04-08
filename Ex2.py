from Ex1 import Node




class BinaryTree :
    def __init__(self,root):
        self.__root=root
    def get_root(self):
        return self.__root

    def is_root(self,node):
        if self.__root == node :
            return True
        else :
            return False






if __name__ == '__main__' :
    n1=Node(3)
    n2=Node(4,False,n1)
    n3=Node(6)
    n4=Node(5,n3,n2)
    n5=Node(18)
    n6=Node(21)
    n7=Node(19,n6,n5)
    n8=Node(17,n7)
    nfin=Node(12,n8,n4)
