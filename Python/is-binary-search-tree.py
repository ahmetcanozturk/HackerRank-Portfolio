# solution to the HackerRank problem "Is This a Binary Search Tree?"
# https://www.hackerrank.com/challenges/is-binary-search-tree/problem
# Given the root node of a binary tree, can you determine if it's also a binary search tree?
# Ahmetcan Ozturk

import math

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    result = isBST(root, -math.inf)
    if(result):
        print("Yes")
    else:
        print("No")

def isBST(root, previous):
    if root != None:
        if not isBST(root.left, previous):
            return False

        if (root.data <= previous):
            return False

        previous = root.data

        return isBST(root.right, previous)
    return True

if __name__ == "__main__":
    root = node(5)
    root.left = node(7)
    root.right = node(9)
    root.left.left = node(6)
    root.left.right = node(11)

    check_binary_search_tree_(root)