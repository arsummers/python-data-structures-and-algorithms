from tree import BinaryTree, Node

def tree_intersection(tree_1, tree_2):

    tree_1_results = tree_1.in_order()
    tree_2_results = tree_2.in_order()

    duplicates = []

    for num in tree_1_results:
        if num in tree_2_results:
            duplicates.append(num)
    return duplicates
