# Traversals
# Visiting every single node
# O(n)

from performance import timer
from binary_search import BinaryTree, Node


def breadthFirstSearch(tree: BinaryTree) -> list:
    currentNode: Node = tree.root
    search_list: list = []
    queue: list = []
    queue.append(currentNode)
    
    while(queue):
        currentNode = queue.pop(0)
        search_list.append(currentNode.value)
        if (currentNode.left):
            queue.append(currentNode.left)
        if (currentNode.right):
            queue.append(currentNode.right)
        
    return search_list

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

    # to return BFS [9, 4, 20, 1, 6, 15, 170]
        
        
        
    
    
    