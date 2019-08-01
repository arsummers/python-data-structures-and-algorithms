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

tree = BinaryTree()
def find_maximum_value(tree):

    results = []

    def visit(node):
        if node.left:
            visit(node.left)

        results.append(node.value)

        if node.right:
            visit(node.right)

    visit(tree.root)
    return max(results) 

def find_maximum_value_other_way(tree):
    current_max = tree.root.value

    def visit(node):
        nonlocal current_max
        if node.left:
            visit(node.left)

            if node.left.value > current_max:
                current_max = node.left.value

        if node.right:
            visit(node.left)

            if node.right.value > current_max:
                current_max = node.right.value
        
    visit(tree.root)
    return current_max
