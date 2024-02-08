from __future__ import annotations
import sys
from collections import deque
sys.setrecursionlimit(10**6)

# class Node:
#     def __init__(self, data: int, left: Node = None, right: Node = None):
#         self.data = data
#         self.left = left
#         self.right = right


#     def insert(self, data: int) -> None:
#         if self.data == None:
#             self.data = data
#         else:
#             if data <= self.data:
#                 if self.left == None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right == None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)

def printPostorder(root: list[int], i: int = 0) -> None:
    if len(root) == i:
        return
        
    templist = []

    if root[i] > root[i + 1]:
        printPostorder(root, i+1)
    else:
        while root[i - 1] > root[i]:
            templist.append(root.pop(i))
        while templist:
            print(templist.pop())


if __name__ == "__main__":
    root = []

    while True:
        try:
            root.append(int(sys.stdin.readline()))
        except:
            break

    printPostorder(root)