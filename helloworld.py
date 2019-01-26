import smtplib
from email.message import EmailMessage

import urllib.parse as urlparse
from urllib.parse import urlencode

from flask import Flask, request, redirect, abort, jsonify
from flask_cors import CORS
import database



app = Flask(__name__)
CORS(app)
 
URL = "http://127.0.0.1:5500/"
INVITATION_PATH = "invitation.html"

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
       
def get_url_for_id(id):
    params = {'id': id}
    url_parts = list(urlparse.urlparse(URL + INVITATION_PATH))
    url_parts[4] = urlencode(params)
    return urlparse.urlunparse(url_parts)



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
    #m = meeting(name, date, time, location, description)
    id = database.insert_meeting(name, date, time, location, description)
    
    return redirect(get_url_for_id(id))

@app.route('/getMeeting' , methods = ['GET'])
def get_meeting():
    meeting_id = request.args["id"]
    meeting_tuple = database.get_meeting(meeting_id)
    print(meeting)
    meeting_data = {}
    meeting_data['name'] = meeting_tuple[1]
    meeting_data['date'] = meeting_tuple[2]
    meeting_data['time'] = meeting_tuple[3]
    meeting_data['location'] = meeting_tuple[4]
    meeting_data['description'] = meeting_tuple[5]
    return jsonify(meeting_data)



@app.route('/email', methods = ['POST'])
def email_stuff():
    print("Hello There")
    return "Ingore not implemented yet"




    

