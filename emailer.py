import pandas as pd
import smtplib

e = pd.read_excel("Excel File here") #add name/location of excel file containing emails
emails = e['Emails'].values
#returns all email values as a list

server = smtplib.SMTP("server", port_number) #replace port_number with the port number you will be using
serevr.starttls()
server.login("email", "password")
#message content below
msg = "Message Content Here"
subject = "Subject here"
body = "Subject: {}\n\n{}".format(subject, msg)

for email in emails:
    server.sendmail("email to send from", email, body)
server.quit()