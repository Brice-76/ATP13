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


if  __name__ =='__main__' :
# root
    N1=Node(12)
    Tree=BinaryTree(N1)
# première ligne
    N2=Node(5)
    N3=Node(17)
    N1.set_left(N2)
    N1.set_right(N3)
# deuxieme ligne
    N4=Node(4)
    N5=Node(6)
    N6=Node(19)
    N2.set_left(N4)
    N2.set_right(N5)
    N3.set_right(N6)
# troisieme ligne
    N7=Node(3)
    N8=Node(18)
    N9=Node(21)
    N4.set_left(N7)
    N6.set_right(N8)
    N6.set_right(N9)

# if __name__ == '__main__' : # a faire avec des set...
#     n1=Node(3)
#     n2=Node(4,None,n1)
#     n3=Node(6)
#     n4=Node(5,n3,n2)
#     n5=Node(18)
#     n6=Node(21)
#     n7=Node(19,n6,n5)
#     n8=Node(17,n7)
#     nfin=Node(12,n8,n4)
#
#
#     Tree=BinaryTree(nfin)
#     Tree.size(nfin)
