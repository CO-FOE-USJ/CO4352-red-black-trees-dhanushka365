# 18/ENG/112
import sys
# Node creation
class Node:
    def __init__(self, item):
        self.item = item #data in the node
        self.parent = None#parent node
        self.left = None#left child
        self.right = None#right child
        self.color = 1#1=RED


class RedBlackTree:
    def __init__(self):#construtor to store node details
        self.TNULL = Node(0)
        self.TNULL.color = 0#black
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL#root node

    # Preorder
    def pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.item:#if the key(data)of the node is found,the node is returened
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)

            if node.item != self.root.item:
                if last:
                    sys.stdout.write("└──")
                    indent += "     "
                else:
                    sys.stdout.write("├──")
                    indent += "|    "

            s_color = "R" if node.color == 1 else "B"
            print(s_color + str(node.item))
            if node.left == self.TNULL:
                self.__print_helper(node.right, indent, True)
            else:
                self.__print_helper(node.right, indent, False)
            self.__print_helper(node.left, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        if self.search_tree_helper(self.root, k).item == k:
            return True
        else:
            return False

     #to search min value
    def minimum(self):
        if self.root:
            return self._minimum(self.root)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')    

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    #to search max value
    def maximum(self):
        if self.root:
            return self._maximum(self.root)
        else:
            raise ValueError('The tree is empty!')

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node
    
  
    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)#set the key value to node variable
        node.parent = None
        node.item = key#inserting the value(key) to the node
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root
    #if there is one node this will execute
        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y# setting the ne parent
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)



if __name__ == "__main__":

    bst = RedBlackTree()#object creation
    
    initial_inputs = [int(x) for x in input().split()]
    for value in initial_inputs:
        bst.insert(value)
    print()   
    bst.print_tree()
    #print("\n")
    # take the number of opeerations
    num_commands = int(input())

if num_commands >0:
    for i in range(num_commands):
        temp_input = input().split()
        #check the operation
        if temp_input[0] == "Delete":
            bst.delete_node(int(temp_input[1]))
            print()
            bst.print_tree()
            #print("\n")
        elif temp_input[0] == "Search":
            print()
            print(bst.searchTree(int(temp_input[1])))
            #print("\n")
        elif temp_input[0] == "Min":
            print()
            print(bst.minimum(bst.root).item)
            #print("\n")    
        elif temp_input[0] == "Max":
            print()
            print(bst.maximum(bst.root).item)
        else:
            print("\n")

else:
    print("Please enter a valid value for command ")
print("\n")    
