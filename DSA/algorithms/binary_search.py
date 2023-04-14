# Binary Search

# Store data into a Binary Tree
# For sorted elements 

# Best O(1) 
# Worst O(log(n))



import random     
from functools import cache   
from performance import timer  


class Node():
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value: int = value
        self.left: Node | None = left
        self.right: Node | None = right
    
    def __repr__(self):
        return f"{self.__dict__}"
        

def insert_node(node: Node, new_node: Node):
    if new_node.value < node.value:
        if node.left == None:
            node.left = new_node
            return
        insert_node(node.left, new_node)
        return
    if new_node.value > node.value:
        if node.right == None:
            node.right = new_node
            return
        insert_node(node.right, new_node)
        return


class BinaryTree:
    def __init__(self, value: int):
        self.root: Node = Node(value)
    
    def add_value(self, value):
        new_node = Node(value)
        insert_node(self.root, new_node)
    
    def lookup(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
               return f"found {current_node.value}"
            elif value < current_node.value:
               current_node = current_node.left
            else: 
               current_node = current_node.right
        return "not found"
        
    def find_value(self, value):
        raise NotImplementedError("Code not found")
        
    def print_tree(self):
        print(self.root)


if __name__ == "__main__":
    
    bt = BinaryTree(500000)
    
    with timer("insertion"):
        for _ in range(1000000):
            bt.add_value(random.randint(0, 1000000))

    with timer("binary search"):
        print(bt.lookup(10))

    
                
                
        
        
        
        
    







