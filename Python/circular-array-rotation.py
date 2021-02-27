# solution to the HackerRank problem "Circular Array Rotation"
# https://www.hackerrank.com/challenges/circular-array-rotation/problem
# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.
# Ahmetcan Ozturk 
def circularArrayRotation(a, k, queries):
    result = []
    i = 0
    while i < k:
        elm = a.pop(len(a)-1)
        a.insert(0, elm)
        i = i + 1
    
    for q in queries:
        result.append(a[q])

    return result

if __name__ == "__main__":
    print("nkq: ")
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    print("array: ")
    arr = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(arr, k, queries)

    print("output: ")
    print('\n'.join(map(str, result)))
    print('\n')