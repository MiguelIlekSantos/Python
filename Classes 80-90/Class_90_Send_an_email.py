import smtplib

sender = "rabibaral3@gmail.com"
reciever = "baralsabin441@gmail.com"
password = "Rabi123456789+"
subject =  "Phyton email test"
body = "I wrote and rmail in phyton"

#Header
message = f"""from: Snoop dog {sender}  
To: {reciever}
subject: {subject}\n
{body}

"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender,password)
    print("logged in....")
    server.sendmail(sender,reciever, message)
    print("Email Has been Sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")