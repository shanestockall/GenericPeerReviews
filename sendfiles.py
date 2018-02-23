import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os
import pandas
import time

# Your email and password here, as strings
EMAIL = ""
PASSWORD = ""

# The name of the assignment (e.g. Homework 1) - used in lines 55, 57
ASSIGNMENT = ""


def main():
	roster = pandas.read_csv('roster.csv')
	emails = list(roster.email)
	student_ids = list(roster.id)
	list_ids = []
	for file in os.listdir('./tosend/'):
		list_ids.append(file[1:-5])

	student_ids = map(str, student_ids)

	print list_ids
	print student_ids

	for student_id in list_ids: 
		if student_id in student_ids: 
			for student in student_ids: 
				if str(student) == student_id:
					index = student_ids.index(student)
					email = emails[index]
					try:
						print 'sending files to ' + str(email)
						send_mail(email, student_ids[index])
					except: 
						time.sleep(300)
						list_ids.append(student_ids[index])
						continue





def send_mail(recipient, id):
    msg = MIMEMultipart()
    msg['From'] = "EMAIL"
    msg['To'] = recipient
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Peer Reviews for " + ASSIGNMENT

    text = "Hello, " + recipient[:-25] + ". Please find attached your peer reviews for " + ASSIGNMENT  +". You should use the rubric and CSV template on Canvas to grade. These will be due " + DATE

    msg.attach(MIMEText(text))

    f = open("./tosend/_" + id + "_.zip", "rb")
    part = MIMEApplication(
    	f.read(),
    	Name="./tosend/_" + id + "_.zip")

    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename=%s' % str(id) + ".zip"
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("EMAIL", "PASSWORD")
    s.sendmail("EMAIL", recipient, msg.as_string())
    s.close()


if __name__ == '__main__':
	main()
