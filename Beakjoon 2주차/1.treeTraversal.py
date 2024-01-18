from __future__ import annotations
from typing import Any

import sys

class Node:
    def __init__(self, data: Any, left: Node = None, right: Node = None):
        self.data = data
        self.left = left
        self.right = right


    def insert(self, data: list[str]) -> None:
        if self.data == None:
            self.data = data[0]

        here_node = self.heresNode(data[0])

        if here_node.data == data[0]:
            if data[1] != "." and here_node.left == None:
                here_node.left = Node(data[1])
            if data[2] != "." and here_node.right == None:
                here_node.right = Node(data[2])

    
    def heresNode(self, value: Any) -> Node:
        if not self.data:
            return None
        
        if self.data == value:
            return self
        if self.left:
            if (here_node := self.left.heresNode(value)) != None:
                return here_node
        if self.right:
            if (here_node := self.right.heresNode(value)) != None:
                return here_node
            

def preorderTrav(self: Node) -> None:
    if self == None:
        return
    
    print(self.data, end="")
    preorderTrav(self.left)
    preorderTrav(self.right)


def inorderTrav(self: Node) -> None:
    if self == None:
        return
    
    inorderTrav(self.left)
    print(self.data, end="")
    inorderTrav(self.right)


def postorderTrav(self: Node) -> None:
    if self == None:
        return
    
    postorderTrav(self.left)
    postorderTrav(self.right)
    print(self.data, end="")
        

class BinarySearchTree:
    def __init__(self):
        self.root = None


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    root = Node(None)

    if 0 < N < 27:
        
        for _ in range(N):
            input = sys.stdin.readline()[:-1].split()
            root.insert(input)

    preorderTrav(root)
    print()
    inorderTrav(root)
    print()
    postorderTrav(root)