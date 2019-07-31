import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
   
    def __init__(self):
        self.front = self.rear = None

        def peek(self):
            return self.front and self.front.value

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

    def breadth_first(self):
        results = []
        queue = Queue()
        working_queue = collections.deque([])

        def handle_tree(tree):
            while queue.peek():
                results.append(working_queue.pop())

                if queue.front.left is not None:
                    results.append(working_queue.pop())
                
                if queue.front.right is not None:
                    results.append(working_queue.pop())


        queue.append(self.root)
        
        # do things that put it into list. print each thing in the list
        def printing_time():
            for item in results:
                print(item)
        printing_time() 

