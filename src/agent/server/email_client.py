import email
import smtplib


msg = email.message_from_string('warning')
msg['From'] = "matabotmin@outlook.com"
msg['To'] = "pcyuen98@gmail.com"
msg['Subject'] = "helOoooOo"
msg['Body'] = "Test"

s = smtplib.SMTP("smtp-mail.outlook.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('matabotmin@outlook.com', 'Eyebotmin0.')

s.sendmail("admin@eye-bot.com", "pcyuen98@gmail.com", msg.as_string())

s.quit()