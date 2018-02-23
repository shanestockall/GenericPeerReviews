#Sending out Peer Reviews

1. Download Canvas Gradebook
2. Delete every column that isn't ID and Netid, save as gradebook.csv
3. Run fixroster.py in terminal
4. Download submissions from Canvas, unzip into ./submissions
5. Run peerreviews.py in terminal
6. You should now have a master.csv - this matches canvas ID to 3 other Canvas IDs -- peer reviewer to peer reviewees. In ./to_send there are now zipfiles with 3 other zipfiles, the containing zip is the canvas id of the reviewer, the 3 contained zips are the canvas ids of the reviewees. 
7. Edit the globals EMAIL, PASSWORD, and ASSIGNMENT in senfiles.py to reflect the email you wish to send the email from and the assignment you're sending the review files from 
8. It might be good to send a test email, replace recipient in line 53 with EMAIL. Run sendfiles.py, get through one loop of the code, and then ctrl+c to exit. You should now have an email with what the first person in the list will see. 
9. Replace EMAIL with recipient in line 53 to send it to the class. 
10. Run sendfiles.py in terminal 

Congrats! You just sent peer reviews to everyone in the class. :) 