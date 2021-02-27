# solution to the HackerRank problem "Binary Search Tree : Insertion"
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
# Insert the values into their appropriate position in the bst and return the root of the updated tree.
# Ahmetcan Ozturk 
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        inserted = False
        if self.root == None:
            self.root = Node(val)
        else:
            node = self.root
            while not inserted:
                if val < node.info:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(val)
                        inserted = True
                elif val > node.info:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(val)
                        inserted = True
                else:
                    inserted = True

    def preOrder(self, root):
        if(root == None):
            return
        print(root.info, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)

if __name__ == "__main__":
    tree = BinarySearchTree()
    arr = [4, 2, 3, 1, 7, 6]
    for i in range(len(arr)):
        tree.insert(arr[i])

    tree.preOrder(tree.root)
