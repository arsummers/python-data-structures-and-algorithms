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
    def __init__(self):
        self.root = None

    def add(self, value):

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

        # def find_position(node):
            # if node is None:
            #     node = self.root

        #     else:
        #         if value < node.value:
        #             breakpoint()
        #             if node.right is None:
        #                 node.right = node
        #             else:
        #                 # self.root.left = node.value
        #                 find_position(node.right)
                        
        #         else:
        #             if node.left is None:
        #                 node.left = node
        #             else:
        #                 # root.right = node.value
        #                 find_position(node.left)

        #     else:
        #         if value < node.value:
        #             if node.right is None:
        #                 node.right = Node(value)

        # if not self.root:
        #     self.root = Node(value)
        #     return


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
     

                            
        # find_position(self.root)            
                
       
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