import smtplib

sender1 = 'youremail@gmail.com'
sender2 = 'youremail@gmail.com'
sender3 = 'youremail@gmail.com'
sender4 = 'youremail@gmail.com'
sender5 = 'youremail@gmail.com'

password = 'yourEmailPassword'

rec = 'theirnumber@provider'

#Message you want to send.
message = """Ham bone chicken wing"""

s1 = smtplib.SMTP("smtp.gmail.com", 587)
s1.starttls()
s1.login(sender1,password)

s2 = smtplib.SMTP("smtp.gmail.com", 587)
s2.starttls()
s2.login(sender2,password)

s3 = smtplib.SMTP("smtp.gmail.com", 587)
s3.starttls()
s3.login(sender3,password)

s4 = smtplib.SMTP("smtp.gmail.com", 587)
s4.starttls()
s4.login(sender4,password)

s5 = smtplib.SMTP("smtp.gmail.com", 587)
s5.starttls()
s5.login(sender5,password)

numberMessagesToSend = 15

for x in range(0,numberMessagesToSend):
    s1.sendmail(sender1, rec, message)
    s2.sendmail(sender2, rec, message)
    s3.sendmail(sender3, rec, message)
    s4.sendmail(sender4, rec, message)
    s5.sendmail(sender5, rec, message)

s.quit()
