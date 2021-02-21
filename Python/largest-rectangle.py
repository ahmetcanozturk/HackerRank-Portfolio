# solution to the HackerRank problem "Largest Rectangle"
# https://www.hackerrank.com/challenges/largest-rectangle/problem
# Real Estate Developers is planning to demolish a number of old buildings and construct a shopping mall
# Task is to find the largest solid area in which the mall can be constructed.
# Ahmetcan Ozturk

def largestRectangle(h):
    if len(h) == 0:
        return 0
    area = 0
    curr = 0

    for i in range(len(h)):
        j = i - 1
        k = i + 1
        base = 1
        okLeft = True
        okRight = True
        while (okLeft or okRight):
            if j >= 0 and okLeft:
                if (h[j] < h[i]):
                    okLeft = False
                else:
                    base = base + 1
                j = j - 1
            if j < 0:
                okLeft = False
            if k < len(h) and okRight:
                if (h[k] < h[i]):
                    okRight = False
                else:
                    base = base + 1
                k = k + 1
            if k == len(h):
                okRight = False
        curr = h[i] * base
        if curr > area:
            area = curr
   
    return area

if __name__ == "__main__":
    #h = [1,2,3,4,5]
    #h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
    n = int(input())
    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)
    
    print(result)