import smtplib
from email.message import EmailMessage

import urllib.parse as urlparse
from urllib.parse import urlencode

from flask import Flask, request, redirect, abort
from emailer import sendTestEmail

app = Flask(__name__)
 
URL = "http://127.0.0.1:5500/"
INVITATION_PATH = "invitation.html"


class post:
    def __init(self, text):
        self.text = text
        self.votes = 0

    def increaseVote(self):
        self.votes += 1
    
    def decreaseVote(self):
        self.votes -=1 

class chat:
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)

    def get_ordered_post(self, post):
        return self.posts

class meeting:
    def __init__(self, name, date, time, location, description):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.description = description
    
    def get_url(self):
        params = {'name': self.name, 'date' : self.date , 'time' : self.time, 'location' : self.location, 'description' :  self.description}
        url_parts = list(urlparse.urlparse(URL + INVITATION_PATH))
        url_parts[4] = urlencode(params)
        return urlparse.urlunparse(url_parts)
    
    def __str__(self):
        return 'name:\t' + str(self.name) + \
               '\ndate:\t' + str(self.date) + \
               '\ntime:\t' + str(self.time) + \
               '\nlocation:\t' + str(self.location) + \
               '\ndescriptions:\t' + str(self.description)  
       
      
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
    location = request.form['location']
    m = meeting(name, date, time, location, description)
    return redirect(m.get_url())

@app.route('/email', methods = ['POST'])
def email_stuff():
    sendTestEmail()
    return "stuff"




    

