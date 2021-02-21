# solution to the HackerRank problem "Mini-Max Sum"
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Ahmetcan Ozturk

import math

def miniMaxSum(arr):
    minimum = math.inf
    maximum = -math.inf
    miniSum = 0
    maxiSum = 0
    for elm in arr:
        miniSum += elm
        maxiSum += elm
        if elm < minimum:
            minimum = elm
        if elm > maximum:
            maximum = elm
    
    miniSum = miniSum - maximum
    maxiSum = maxiSum - minimum
    print (str(miniSum) + " " + str(maxiSum))

if __name__ == "__main__":
    arr = [10, 5, 3, 12, 11, 20, 9]

    miniMaxSum(arr)