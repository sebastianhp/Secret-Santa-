import random
import os

names = ['Sebastian', 'Lucas F', 'Ian L', 'David S', 'Tae', 'Sarah', 'Grace', 'Tasha', 'Lucas S', 'Andrew', 'Mariana', 'Chris', 'Ian D']

random.seed()
pickedind = []
pickednames = []
for i in range(len(names)):
	repick = True
	while repick:
		index = random.randint(0,len(names)-1)
		if index == i:
			repick = True
		else:
			repick = index in pickedind
	pickedind.append(index)
	pickednames.append(names[index])

	fname = names[i].replace(' ', '_')
	cmd = 'echo \"' + names[index] + '\" > ./files/' + fname + '.txt'
	os.system(cmd)	
	#print names[index] + '\t' + names[i]

for i in range(0,len(pickednames)-1):
		if pickednames[i] == pickednames[i+1]:
				print 'duplicate'
