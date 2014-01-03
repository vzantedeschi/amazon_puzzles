import string
letters = string.lowercase + string.uppercase

input = map(str,raw_input().split())
words = []
for w in input:
    for c in w:
        if c not in letters:
            w = w.replace(c,'')
    words.append(w)    

n = int(raw_input())
targets = []

for i in range(n):
    targets.append(str(raw_input()).lower())
    
output = []

i = 0

for w in words:
	
    if w in targets:
        i += 1
        output.append([])
		
    for j in range(i):
		
        for t in targets:
            
            if t not in [l.lower() for l in output[j]]:
                output[j].append(w)
                break

dummy = []
for t in targets:

    for o in output:
        
        if t in [l.lower() for l in o]:
            dummy.append(o)
            
    output = dummy
    dummy = []
    
minLen = -1
segment = []	

for o in output:
	
    if len(o) < minLen or minLen < 0:
          
        minLen = len(o)
        segment = o

        line = ''

for s in segment:
    line += s + ' '
	
if minLen < 0:
    line = 'NO SUBSEGMENT FOUND'
    
print line