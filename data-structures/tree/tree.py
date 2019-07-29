class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self):
        results = []

        def visit(node):
            # visits left node
            if node.left:
                visit(node.left)

            #adds node
            results.append(node.value)

            # visits right node:
            if node.right:
                visit(node.right)

        visit(self.root)
        return results

    def pre_order(self):
        results = []

        def visit(node):
            
            results.append(node.value)

            if node.left:
                visit(node.left)

            if node.right:
                visit(node.right)       

        visit(self.root)
        return results

    def post_order(self):
        results = []

        def visit(node):
            if node.left:
                visit(node.left)

            if node.right:
                visit(node.right) 

            results.append(node.value)

        visit(self.root)
        return results




class BinarySearchTree:
    # https://www.youtube.com/watch?v=yC83Kp2xig8
    def __init__(self):
        self.root = None

    def add(self, value):

        if self.root is None:
            self.root = Node(value)

        else:
            self.find_position(value, self.root)

    def find_position(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.find_position(value, current_node.left)

        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.find_position(value, current_node.right)
              
                
       
    def contains(self, value, node):
        
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return contains(value, node.left_child)
        else:
            return contains(value, node.right_child)
        # returns a boolean representing if the value appears in the tree or not
        # if self == null
            # return false
        # if key == search value
            # return true
        # if key < search value
            # search to the right
        # otherwise search to the left