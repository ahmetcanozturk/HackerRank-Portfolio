# solution to the HackerRank problem "Encryption"
# https://www.hackerrank.com/challenges/encryption/problem
# Create a function to encode a message.
# Ahmetcan Ozturk
import math
def encryption(s):
    sn = s.replace(" ", "")
    l = len(sn)
    rows = math.floor(math.sqrt(l))
    cols = math.ceil(math.sqrt(l))
    if (rows * cols < l):
        rows = cols

    arr = [""] * (rows * cols)
    row = -1
    for i in range(l):
        if i % cols == 0:
            row = row + 1
        loc = ((i % cols) * rows) + row
        arr[loc] = str(sn[i])

    result = []
    for i in range(len(arr)):
        if (i % rows == 0 and i > 0):
            result.append(" ")
        result.append(arr[i])

    return "".join(result)

if __name__ == '__main__':
    print("string: ")
    s = input()

    result = encryption(s)

    print("output :\n" + result + '\n')