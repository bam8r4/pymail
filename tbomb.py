import smtplib

sender = 'youremail@gmail.com'
rec = 'theirnumber@provider'

password = 'yourEmailPassword'

#Message you want to send.
message = """Ham bone chicken wing"""

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(sender,password)

numberMessagesToSend = 15

for x in range(0,numberMessagesToSend):
    s.sendmail(sender, rec, message)

s.quit()
