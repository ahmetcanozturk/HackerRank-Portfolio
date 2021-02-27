# solution to the HackerRank problem "Count Triplets"
# https://www.hackerrank.com/challenges/count-triplets-1/problem
# It should return the number of triplets forming a geometric progression for a given r as an integer.
# Ahmetcan Ozturk 
def countTriplets(arr, r):
    count = 0
    d = { }
    dc = { }
    for i in range(len(arr)):
        item = arr[i]
        key = item / r

        if (key in dc and item % r == 0):
            count = count + dc[key]

        if (key in d and item % r == 0):
            c = d[key]
            if item in dc:
                dc[item] = dc[item] + c
            else:
                dc[item] = c

        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1

    return count

if __name__ == '__main__':
    print("n and r: ")
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])

    print("array: ")
    arr = list(map(int, input().rstrip().split()))

    result = countTriplets(arr, r)

    print("output :\n" + str(result) + '\n')
