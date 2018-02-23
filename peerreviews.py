import glob
import os
import csv
from zipfile import ZipFile
import re
import random


# get list of submissions
listFiles = glob.glob("./submissions/*.zip")

# initialize list of students 
listStudents = []

# call a write file
writeFileName = "master.csv"
writeFile = open(writeFileName, 'w+')
writeFile.write("Grader ID, Peer Reviews \n")

random.shuffle(listFiles)

# rename to only include student id
for i in range(0, len(listFiles)):
	file = listFiles[i]
	print "file = " + str(file)
	studentID = re.search("_[0-9]{4,6}_", str(file)).group(0)
	# memoize student IDs, because we're good little programmers
	listStudents.append(str(studentID))
	print 'ID: ' + str(studentID)
	os.rename(file, './submissions/' + str(studentID) + ".zip")
	file = './submissions/' + str(studentID) + ".zip"
	listFiles[i] = file


for i in range(0, len(listFiles)):
	studentID = listStudents[i]
	peerReviews = []
	reviewFiles = []
	
	# prep zip file
	with ZipFile('./tosend/' + studentID + '.zip', 'w') as myZip: 

		# the case where the list wraps
		if listStudents[i] == listStudents[-1]:
			peerReviews = listStudents[0:3]
			reviewFiles = listFiles[0:3]

		elif listStudents[i] == listStudents[-2]:
			peerReviews = listStudents[0:2] + [listStudents[i + 1]]
			reviewFiles = listFiles[0:2] + [listStudents[i + 1]]

		elif listStudents[i] == listStudents[-3]:
			peerReviews = [listStudents[0]] + listStudents[i + 1: i + 3]
			reviewFiles = [listFiles[0]] + listFiles[i + 1: i + 3]
		# the list doesn't wrap 
		else: 
			peerReviews = listStudents[i+1:i+4]
			reviewFiles = listFiles[i+1:i+4]

		# write review files to zip archive
		for file in reviewFiles: 
			try: 
				myZip.write(file)
			# the last one throws an exception, but the file still gets made, so we can pass it
			except Exception as e:
				pass

		myZip.close()

	# add pairs to CSV for logging purposes
	writeFile.write(studentID + ", " + str(peerReviews) + "\n")

	


