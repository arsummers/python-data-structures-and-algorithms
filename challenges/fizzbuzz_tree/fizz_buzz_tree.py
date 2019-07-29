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

def fizz_buzz_tree(tree):
    
    def visit(node):

        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'

        elif node.value % 3 == 0:
            node.value = 'fizz'
        
        elif node.value % 5 == 0:
            node.value = 'buzz'


        if node.left:
            visit(node.left)
        if node.right:
            visit(node.right)

    visit(tree.root)
    return tree

