# solution to the HackerRank problem "Maximum Element"
# https://www.hackerrank.com/challenges/maximum-element/problem
# You have an empty sequence, and you will be given N queries. Each query is one of these three types:
# push the element x into the stack, delete the element present at the top of the stack, print the maximum element in the stack.
# Ahmetcan Ozturk

import math

class SpecialMaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = [-math.inf]

    def push(self, x):
        self.stack.append(x)
        if (x >= self.maxStack[-1]):
            self.maxStack.append(x)

    def delete(self):
        elm = self.stack.pop(len(self.stack) - 1)
        if (elm == self.maxStack[-1]):
            self.maxStack.pop(len(self.maxStack) - 1)

    def printMax(self):
        print(self.maxStack[-1])

if __name__ == "__main__":
    specialStack = SpecialMaxStack()
    q = int(input())
    i = 0
    while i < q:
        op = input()
        if " " in op:
            arr = op.split(" ")
            cmd = int(arr[0])
            param = int(arr[1])
            if (cmd == 1):
                specialStack.push(param)
        else:
            cmd = int(op)
            if (cmd == 2):
                specialStack.delete()
            elif (cmd == 3):
                specialStack.printMax()
        i = i + 1