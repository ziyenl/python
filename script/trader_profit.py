#!/bin/python3
#https://www.hackerrank.com/contests/gs-codesprint/challenges/trader-profit
#Algorithm


import sys

def traderProfit(k, n, A):
    if k == 0:
        return 0
    current_best = 0
    for start in range(len(A)-1):
        for end in range(start+1, len(A)):
            if A[end] > A[start]:
                diff = A[end] - A[start]
                diff = diff + traderProfit(k-1, n, A[end+1:])
                current_best = max(diff, current_best)
    return current_best


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        k = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = traderProfit(k, n, arr)
        print(result)
