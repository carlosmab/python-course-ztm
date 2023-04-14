# Traversals
# Visiting every single node
# O(n)

from performance import timer
from binary_search import BinaryTree, Node


def breadthFirstSearch(tree: BinaryTree) -> list:
    current_node: Node = tree.root
    search_list: list = []
    queue: list = []
    queue.append(current_node)
    
    while queue:
        current_node = queue.pop(0)
        search_list.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        
    return search_list


def breadthFirstSearchRecursive(queue: list = [], search_list: list = []) -> list:
    if not queue: return search_list
    
    current_node = queue.pop(0)
    search_list.append(current_node.value)
    
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
    return breadthFirstSearchRecursive(queue, search_list)


if __name__ == "__main__":
    bt = BinaryTree(9)
    bt.add_value(4)
    bt.add_value(6)
    bt.add_value(20)
    bt.add_value(170)
    bt.add_value(15)
    bt.add_value(1)

    with timer("BFS"):
        print(breadthFirstSearch(bt))
        
    with timer("\nRecursive"):
        queue = [bt.root]
        print(breadthFirstSearchRecursive(queue, []))

    # to return BFS [9, 4, 20, 1, 6, 15, 170]
        
        
        
    
    
    