
nbSlots, duration = raw_input().split()
nbSlots, duration = int(nbSlots), int(duration)

busyTime = set()

for i in range(nbSlots):
	startH, startM, endH, endM = raw_input().split()
	startH, startM, endH, endM = int(startH), int(startM), int(endH), int(endM)

	startParse = startH * 60 + startM
	endParse = endH * 60 + endM

	[busyTime.add(t) for t in range(startParse, endParse)]

solutions = []
dummy = []

s = 0
for n in range(24 * 60):

	if n in busyTime:
		if n - s >= duration:
			solutions.append([s, n])
		s = n + 1

if 24 * 60 - s >= duration:
	solutions.append([s, n]) 

for s in solutions:

	startH = s[0] / 60
	startM = s[0] - startH * 60

	endH = s[1] / 60
	endM = s[1] - endH * 60

	if startH < 10:
		startH = '0' + str(startH)

	if startM < 10:
		startM = '0' + str(startM)

	if endH == 23 and endM == 59:
		endH = 0
		endM = 0
	
	if endH < 10:
		endH = '0' + str(endH)

	if endM < 10:
		endM = '0' + str(endM)

	print startH, startM, endH, endM 
