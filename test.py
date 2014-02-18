import sys
import random
new = list()
newnew= list()
big_lines= list()
future_lines = list()
lines = list()
total = ''
h = open('BIG2.txt')
f = open('FUTURE.txt')
for line in h:
	line = line.replace('Donny', 'Doc')
	line = line.replace('Dude', 'Doc')
	big_lines.append(line)


for x in range(0,len(big_lines)):
	if "WALTER" in big_lines[x]:
		for y in range(0,len(big_lines)-x):
			if big_lines[x+y] == "\n":
				if len(total)>0:
					new.append(total)
					total = ''
					break
			else:
				i = big_lines[x+1+y].strip()
				if big_lines[x+y].strip() == "WALTER":
					j = big_lines[x+y].strip()
					total = total + j+ ':' + ' ' +i
				else:
					total = total + ' ' +i




for line in f:
	line = line.strip()
	future_lines.append(line)

for x in range(0,len(future_lines)):
	if future_lines[x] == "PROF. BROWN":
		if future_lines[x+1][0:1] != "(":
			future_lines[x+1] = future_lines[x+1].replace('Marty', 'Walter')
			newnew.append('DOC: '+future_lines[x+1])
  		
		else:
			future_lines[x+2] = future_lines[x+2].replace('Marty', 'Walter')
			newnew.append('DOC: ' +future_lines[x+2])
			


if len(new)>len(newnew):	
	for x in range(0,len(newnew)):
		print new[x]
		print newnew[x]
else: 
	for x in range(0,len(new)):
		print new[x]
		print newnew[x]


