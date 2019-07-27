class Node:
    def __init__(self, value, left=None, right=None):
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
    def __init__(self):
        # self.value = value
        self.root = None
        # self.left = None
        # self.right = None


    def add(self, value):
        # node is the insertion point



        # if value < node.value:
        #     if node.left is None:
        #         node.left = TreeNode(value)
        #     else:
        #         add(value, node.left

        # elif value > node.value:
        #     if node.right is None:
        #         node.right = TreeNode(value)
        #     else:
        #         add(value, node.right

        def find_position(node):
            if node is None:
                node = self.root

            else:
                if value < node.value:
                    if node.right is None:
                        node.right = node
                    else:
                        # root.left = node.value
                        find_position(node.right)
                    
                else:
                    if node.left is None:
                        node.left = node
                    else:
                        # root.right = node.value
                        find_position(node.left)

        if not self.root:
            self.root = Node(value)
            return
                            
        find_position(self.root)            
                
       
    def contains(self, value, node):
        
        if node is None or node.value ==value:
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