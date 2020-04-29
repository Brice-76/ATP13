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


    def size(self,node):
        if node == None :
            return 0
        if node.get_left() == None and node.get_right() == None :
            return 1
        else :
            return 1+self.size(node.get_right())+self.size(node.get_left())
    def size_2(self, node):# professeur
        if node is None:
            return 0
        else:
            return self.size(node.get_left()) + 1 + self.size(node.get_right())


    def print_value(self,node):
        if node == None :
            return
        if node.get_left() == None and node.get_right() ==None :
            print(node)
        else :
            print(node)
            self.print_value(node.get_left())
            self.print_value(node.get_right())

    def print_value_2(self,node):
        if node is None:
            return " "
        else:
            return self.print_value_2(node.get_left()) + self.print_value_2(node.get_right())
    def sum_value(self,node):
        if node== None :
            return 0
        if node.get_left() == None and node.get_right() ==None :
            return node.get_val()
        else :
            return node.get_val()+self.sum_value(node.get_right())+self.sum_value(node.get_left())

    def numberLeaves(self, node) :
        if node==None :
            return 0
        if node.get_left() == None and node.get_right() == None :
            return 1
        else :
            return self.numberLeaves(node.get_right())+self.numberLeaves(node.get_left())

    def numberInternalNodes(self, node) :
        if node== None :
            return 0
        if node.get_left() == None and node.get_right() == None :
            return 0
        else :
            return 1+self.numberInternalNodes(node.get_right())+self.numberInternalNodes(node.get_left())

    def height(self, node) :
        if node is None :
            return 0
        else :
            gauche=1+self.height(node.get_right())
            droite=1+self.height(node.get_left())
            return max(gauche-1,droite-1) # pour enlever la hauteur de la racine

    def belongs(self, node, val) :
        if node is None :
            return 0
        if node.get_val() is val :
            return 1
        else :
            a=self.belongs(node.get_right(),val)
            b=self.belongs(node.get_left(),val)
            if a == 1 or b == 1 :
                return True


    def ancestors(self, node, val, lst=[]) : #qui affiche les antécédents d'un noeud ayant la valeur val
        if node == None :
            return
        else :
            lst.append(node.get_val())
            self.ancestors(node.get_left(),val)
            self.ancestors(node.get_right(),val)
            if val in lst :
                return
    def ancestors_2(self,node,val,lst=[]):






    def descendants(self, node, val) :#qui affiche les descendants d'un noeud ayant la valeur val
        if node is None :
            return False
        if int(node.get_val() )== int(val) :
            print('les descendants sont : ',node.get_right(),node.get_left())
        else :
            self.descendants(node.get_right(),val)
            self.descendants(node.get_left(),val)










if  __name__ =='__main__' :
    N1=Node(12)
    Tree=BinaryTree(N1)
    N2=Node(5)
    N3=Node(17)
    N1.set_left(N2)
    N1.set_right(N3)
    N4=Node(4)
    N5=Node(6)
    N6=Node(19)
    N2.set_left(N4)
    N2.set_right(N5)
    N3.set_right(N6)
    N7=Node(3)
    N8=Node(18)
    N9=Node(21)
    N4.set_left(N7)
    N6.set_left(N8)
    N6.set_right(N9)
    N10=Node(1)
    #N9.set_right(N10)



#
# if __name__ == '__main__' : # a faire avec des set...
#     n6 = Node(6,None,None)
#     n7 = Node(21,None,None)
#     n8 = Node(18,None,None)
#     n9 = Node(3,None,None)
#     n5 = Node(4,None,n9)
#     n4 = Node(19,n7,n8)
#     n3 = Node(17,n4,None)
#     n2 = Node(5,n6,n5)
#     n1 = Node(12, n3, n2)



    Tree=BinaryTree(N1)
    #print(Tree.size(N1))
    #print(Tree.size_2(N1))
    #Tree.print_value(N1)
    #print(Tree.print_value_2(N1))
    #print(Tree.sum_value(N1))
    #print(Tree.numberLeaves(N1))
    #print(Tree.numberInternalNodes(N1))
    #print(Tree.belongs(N1,21))
    #print(Tree.height(N1))
    print(Tree.ancestors(N1,19))
    Tree.descendants(N1,19)

