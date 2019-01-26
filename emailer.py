import sendgrid
import os
from sendgrid.helpers.mail import *


FROM_EMAIL = "meetingsnowdemo@gmail.com"

def send_meeting_invite(email_address, meeting_title, meeting_url):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email(FROM_EMAIL)
    to_email = Email(email_address)
    subject = meeting_title
    content = Content("text/plain", "You have been invited to a meeting, follow this url to get more details:" + meeting_url)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return True if response.status_code == 202 else False
    if response.status_code == 202:
        print(response.status_code)
        print(response.body)
        print(response.headers)


if __name__ == "__main__":
    print(send_meeting_invite("keegan0415dsouza@gmail.com", "Test Email", "https://www.google.com"))