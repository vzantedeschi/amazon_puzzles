#!/usr/bin/env python
# -*- coding: utf-8 -*-

def neighbourhood(t):
	n = [(i,j) for i in range(max(t[0] - 1, 0), min(t[0] + 2, N)) for j in range(max(t[1] - 1, 0), min(t[1] + 2, N))]
	n.remove(t)
	return n

nbTests = int(input())

for i in range(nbTests):

    N = int(raw_input())

    matrix = []
    for n in range(N):
        matrix.append(map(int,raw_input().split()))

    ones = [(i,j) for i in range(N) for j in range(N) if matrix[i][j] == 1]  
    for o in ones:
        nei = neighbourhood(o)
        for n in nei:
        	nei.remove(n)
            if n in ones and n != o:
	            nei.extend(neighbourhood(n))
	            ones.remove(n)
    print len(ones)