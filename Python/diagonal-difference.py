# solution to the HackerRank problem "Diagonal Difference"
# https://www.hackerrank.com/challenges/diagonal-difference/problem
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# Ahmetcan Ozturk 
def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            idx = i*len(arr[i])+j
            if(idx % (len(arr[i])+1) == 0):
                diag1 += arr[i][j]
            if(idx % (len(arr[i])-1) == 0 and idx != 0 and idx != (len(arr)*len(arr[i])-1)):
                diag2 += arr[i][j]
    return abs(diag1 - diag2)

if __name__ == '__main__':
    print("n: ")
    n = int(input().strip())

    arr = []
    print("matrix: ")
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print("output :\n" + str(result) + '\n')