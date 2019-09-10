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

    """ 
    recursively adds values at given points in the Binary Search Tree. Helper function find_position does the dirty work of locating where to put the new node and value
    """  
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
              
                

    """
    Checks to see if the tree contains a given value. Returns a boolean
    """
    def contains_helper(self, value, current_node):
        if value > current_node.value and current_node.right:
            return self.contains_helper(value, current_node.right)
        elif value < current_node.value and current_node.left:
            return self.contains_helper(value, current_node.left)
            
        if value == current_node.value:
            return True 

    def contains(self, value):
        if self.root:

            is_found = self.contains_helper(value, self.root)
            if is_found:
                return True
            return False

        else:
            return None
