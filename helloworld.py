import smtplib
from email.message import EmailMessage

import urllib.parse as urlparse
from urllib.parse import urlencode

from flask import Flask, request, redirect
app = Flask(__name__)
 
URL = "http://127.0.0.1:5500/"
INVITATION_PATH = "invitation.html"

class meeting:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

    def get_url(self):
        params = {'name': self.name, 'date' : self.date , 'description' : self.description}
        url_parts = list(urlparse.urlparse(URL + INVITATION_PATH))
        url_parts[4] = urlencode(params)
        return urlparse.urlunparse(url_parts)
    
    def __str__(self):
        return 'name:\t' + str(self.name) + "\ndate:\t" + str(self.date) + "\ndescriptions:\t" + str(self.description)  
       
      
meetings = []

@app.route('/')
def hello_world():
        return 'hello world'

@app.route('/addData', methods = ['POST'])
def add_meeting():
    name = request.form["name"]
    description = request.form["description"]
    date = request.form['date']
    time = request.form['time']
    print(time)
    m = meeting(name, date, description)
    print(m)
    return redirect(m.get_url())

@app.route('/email', methods = ['POST'])
def email_stuff():
    print("im here")
    me = "keegan0415dsouza@gmail.com"
    you = "keegan0415dsouza@gmail.com"

    s = smtplib.SMTP('localhost')
    s.send_message("Hello There")
    s.quit()
    return True

