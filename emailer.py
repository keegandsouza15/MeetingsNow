import sendgrid
import os
from sendgrid.helpers.mail import *

def sendTestEmail ():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("keegan0415dsouza@gmail.com")
    to_email = Email("keegan0415dsouza@gmail.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == "__main__":
    sendTestEmail()