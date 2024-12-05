'''
Notes:
--no two factor authenticaion...tho i dont know if it exists, i never disabled it if it does.
--port 465 doesnt work - fails immediately
--without TLS line of code ,smtp.starttls(), it fails with " smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server. "
-- I should be able to get it to work with attachement evenaully..
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# initialize connection to our email server, we will use Outlook here
smtp = smtplib.SMTP('smtp.zoho.com', port='587') # smtp = smtplib.SMTP('smtp-mail.outlook.com', port='587') # Note: 465 crashes immediately
smtp.ehlo() # send the extended hello to our server - seems to work without it.
smtp.starttls() # tell server we want to communicate with TLS encryption
smtp.login('matabot@zohomail.com', 'Q9njedjTWy8p') # login to our email server # !Z(favbanfir5)123O

# msg = 'My Test Mail '
msg = MIMEMultipart()
msg['Subject'] = 'This iss thee Subjeccttt'
message = 'This is the boddyyy'
msg.attach(MIMEText(message))

# send our email message 'msg' to our boss
smtp.sendmail('matabot@zohomail.com', 'matabot@zohomail.com', msg.as_string())
smtp.quit()