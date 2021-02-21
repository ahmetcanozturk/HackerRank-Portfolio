# solution to the HackerRank problem "Waiter"
# https://www.hackerrank.com/challenges/waiter/problem
# Ahmetcan Ozturk

def waiter(number, q):
    prime = 1
    A = []
    B = []
    A.append([])
    B.append([])
    for elm in number:
        A[0].append(elm)
    i = 1
    while i <= q:
        A.append([])
        B.append([])
        prime = getIthPrime(i, prime)
        while len(A[i-1]) > 0:
            elm = A[i-1].pop(len(A[i-1]) - 1)
            if (elm % prime == 0):
                B[i].append(elm)
            else:
                A[i].append(elm)
        i = i + 1
    result = []
    for k in range(1, len(B)):
        while len(B[k]) > 0:
            elm = B[k].pop(len(B[k]) - 1)
            result.append(elm)
    while len(A[q]) > 0:
        elm = A[q].pop(len(A[q]) - 1)
        result.append(elm)
    return result

def getIthPrime(idx, lastPrime):
    num = lastPrime
    found = False
    while (not found and num < 1000001):
        prime = True
        j = 2
        while prime and j < num:
            if(num % j == 0):
                prime = False
            j = j + 1
        if (prime and num > lastPrime):
            found = True
        if (not found):
            num = num + 1
    return num

if __name__ == "__main__":
    number = [6, 0, 1, 2, 3]
    q = 4
    result = waiter(number, q)

    print("\n".join(map(str, result)))
