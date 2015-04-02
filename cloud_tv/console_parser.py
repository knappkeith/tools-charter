
a = open('log.txt')
log = []
for line in a:
	log.append(line)
a.close()
keep_going = True
while keep_going:
	answer = raw_input('1 - ERRORs, 2 - Events, 3 - Log, 4 - All, 5 - EXIT, 6 - ReLoad File:')
	print ""
	if answer == '1':
		filter = '[ERROR]'
		print "printing errors"
	elif answer == '2':
		filter = '[EVENT]'
		print "printing events"
	elif answer == '3':
		filter = '[LOG]'
		print "printing log"
	elif answer =='5':
		answer = ""
		keep_going = False
	elif answer == '6':
		a = open('log.txt')
		log = []
		for line in a:
			log.append(line)
		a.close()
		answer = ""
		print "File Reloaded"
	else:
		filter = ' '
		print "printing 'ALL THE THINGS'"
	if answer != "":
		count = 0
		for line in log:
			if filter in line[0:9]:
				count += 1
				print line[0:]
		print ""
		print "There are %d %s entries in the Log!" % (count, filter)
		print ""
