# solution to the HackerRank problem "Equal Stacks"
# https://www.hackerrank.com/challenges/equal-stacks/problem
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 

def equalStacks(h1, h2, h3):
    equal = False
    avg = 0
    firstSum = sum(h1)
    secondSum = sum(h2)
    thirdSum = sum(h3)
    while not equal and len(h1) >= 0 and len(h2) >=0 and len(h3) >= 0:
        allSum = firstSum + secondSum + thirdSum
        avg = int(allSum/3)
        if avg == firstSum and avg == secondSum and avg == thirdSum :
            equal = True
        while (len(h1) > 0 and firstSum > avg):
            elm = h1.pop(0)
            firstSum = firstSum - elm
        while (len(h2) > 0 and secondSum > avg):
            elm = h2.pop(0)
            secondSum = secondSum - elm
        while (len(h3) > 0 and thirdSum > avg):
            elm = h3.pop(0)
            thirdSum = thirdSum - elm
    return avg

def sum(h):
    total = 0
    for elm in h:
        total = total + elm
    return total

if __name__ == "__main__":
    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]
    result = equalStacks(h1, h2, h3)

    print(result)