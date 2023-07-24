import sys
import collections
#import math
#import bisect
import heapq
#import itertools
#import functools
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    kpos = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[i] < a[stack[-1]]:
            curr = stack.pop()
            if kpos[curr] == -1:
                kpos[curr] = i
        stack.append(i)
        print(stack, kpos)
    print()
    ypos = [n] * n
    stack = []
    for i in range(n):
        while stack and a[i] < a[stack[-1]]:
            curr = stack.pop()
            if ypos[curr] == n:
                ypos[curr] = i
        stack.append(i)
        print(stack, ypos)
    print()
    xpos = [-1] * n
    stack = []
    second = []
    for i in range(n - 1, -1, -1):
        while second and a[i] > a[second[-1]]:
            curr = second.pop()
            if xpos[curr] == -1:
                xpos[curr] = i
        temp = []
        while stack and a[i] < a[stack[-1]]:
            curr = stack.pop()
            if xpos[curr] == -1:
                temp.append(curr)
        stack.append(i)
        second += temp[:]
        print(stack, second, xpos)
    res = 0
    for i in range(n):
        res += (kpos[i] - xpos[i]) * (ypos[i] - i)
    print((n - 1) * n * (n + 1) // 6 - res)

t = int(input())
for _ in range(t):
    solve()