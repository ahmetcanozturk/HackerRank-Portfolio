# solution to the HackerRank problem "Simple Text Editor"
# https://www.hackerrank.com/challenges/simple-text-editor/problem
# Implement a simple text editor. Initially, your editor contains an empty string

class SimpleTextEditor:
    def __init__(self):
        self.S = []
        self.opStack = []
        self.paramStack = []

    # append string w
    def append(self, w):
        cArr = list(w)
        self.opStack.append(1)
        self.paramStack.append(w)
        for c in cArr:
            self.S.append(c)

    # delete last k characters
    def delete(self, k):
        self.opStack.append(2)
        w = ""
        i = 0
        while i < k:
            elm = self.S.pop(len(self.S) - 1)
            w = w + elm
            i = i + 1
        self.paramStack.append(w)

    # print the kth character of S
    def print(self, k):
        if len(self.S) >= k:
            print(self.S[k - 1])
        else:
            print("")

    # undo the last (not previously undone) operation
    def undo(self):
        op = self.opStack.pop(len(self.opStack) - 1)
        param = self.paramStack.pop(len(self.paramStack) - 1)
        if op == 1:
            i = 0
            while i < len(param):
                self.S.pop(len(self.S) - 1)
                i = i + 1
        elif op == 2:
            cArr = list(param)[::-1]
            for c in cArr:
                self.S.append(c)

if __name__ == "__main__":
    ste = SimpleTextEditor()

    q = int(input())
    for i in range(q):
        op = input()
        if " " in op:
            opArr = op.split(" ")
            cmd = int(opArr[0])
            param = opArr[1]
            if cmd == 2 or cmd == 3:
                k = int(param)
                if cmd == 2:
                    ste.delete(k)
                else:
                    ste.print(k)
            elif cmd == 1:
                w = param
                ste.append(w)
        else:
            cmd = int(op)
            if cmd == 4:
                ste.undo()