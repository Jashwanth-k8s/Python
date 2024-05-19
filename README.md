# Python

URL: https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

GMAIL Token Creation URL:https://support.google.com/accounts/answer/185833

EMAIL- InstallationPAckage

import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("sender_email_id", "sender_email_id_password")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)
# terminating the session
s.quit()


