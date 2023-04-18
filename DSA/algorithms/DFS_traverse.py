# InOrder = [1, 4, 6, 9, 15, 20, 170]
# PreOrder = [9, 4, 20, 1, 6, 15, 170]
# PostOrder = [1, 6, 4, 15, 170, 20, 9]

from performance import timer
from binary_search import BinaryTree, Node

# In order
def depth_first_search_in_order(tree: BinaryTree) -> list:
    
    def traverse_in_order(node: Node) -> list:
        if node.left:
            traverse_in_order(node.left)
        search_list.append(node.value)
        if node.right:
            traverse_in_order(node.right)
        return search_list
    
    search_list = []
    return traverse_in_order(tree.root)


# Pre order


def depth_first_search_pre_order(tree: BinaryTree) -> list:
    
    def traverse_pre_order(node: Node) -> list:
        search_list.append(node.value)
        if node.left:
            traverse_pre_order(node.left)
        if node.right:
            traverse_pre_order(node.right)
        return search_list
    
    search_list = []
    return traverse_pre_order(tree.root)



# Post order
def depth_first_search_post_order(tree: BinaryTree) -> list:
    
    def traverse_post_order(node: Node) -> list:
        if node.left:
            traverse_post_order(node.left)
        if node.right:
            traverse_post_order(node.right)
        search_list.append(node.value)
        return search_list
    
    search_list = []
    return traverse_post_order(tree.root)



if __name__ == "__main__":
    bt = BinaryTree(9)
    bt.add_value(4)
    bt.add_value(6)
    bt.add_value(20)
    bt.add_value(170)
    bt.add_value(15)
    bt.add_value(1)

    with timer("DFS"):
        print(depth_first_search_in_order(bt))
    
    with timer("DFS"):
        print(depth_first_search_pre_order(bt))

    with timer("DFS"):
        print(depth_first_search_post_order(bt))

    # to return BFS [9, 4, 20, 1, 6, 15, 170]
        
        
        
    
    
    