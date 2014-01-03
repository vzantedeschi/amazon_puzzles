#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbTests = int(input())

def divisers(n):
	d = 5
	div = []
	i = 4
	while d < n / 2:
		if n % d == 0:
			div.append(d)
		d += 6 - i
	div.append(n)
	return div

if 0 < nbTests < 6:
	fibonacci = [5, 8]

	while nbTests > 0:
		nbTests -= 1
		value = int(input())

		if value < 2:
			print "no common divisers"
			continue
		if value % 2 == 0:
			print "2 2"
			continue
		if value % 3 == 0:
			print "3 3"
			continue

		found = False
		div = divisers(value)
		while fibonacci[-1] < div[0]:
			fibonacci.append(fibonacci[-2] + fibonacci[-1])

		for n in fibonacci:
			for d in div:
				if (n % d) == 0:
					print str(n) + ' ' + str(d)
					found = True
					break
			if n == fibonacci[-1] and not found:
				fibonacci.append(fibonacci[-2] + fibonacci[-1])
			if found:
				break
