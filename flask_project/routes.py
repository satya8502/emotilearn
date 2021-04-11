from flask import Flask
from flask import render_template,request
from flask_project import  app
import threading
from PyDictionary import PyDictionary
from flask_project.models import books
import text2emotion as te
from gtts import gTTS
l=[]
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        #self.m=m
    def run(self):
        if(self.threadID==1):
            meaning()
@app.route('/')
def start():
    book=books.query.first()
    print(book.id)
    print(book.author)
    return  render_template("login.html");
@app.route('/home')
def homepage():
    return  render_template('homepage.html')
def textfunc():
   file = open(r"C:\Users\Satya\OneDrive\Desktop\try2.txt","r").read().replace("\n", " ")
   speech = gTTS(text = str(file), lang='en', slow = False)
   speech.save(r"C:\Users\Satya\OneDrive\Desktop\Flask project\flask_project\static\voice1.mp3")
@app.route('/home/audio',methods=['POST','GET'])
def audiopage():
    textfunc()
    if request.method=='GET':
         text="The sky is clear The sun shines bright But out arises a cryptic fear For the future in sight. A pressure to perform, A fear of failure Looming over his thoughts Biting at his confidence Creeping it to naught. Will he fail to be a crusader? But o clarity sets on! As does the sun when the grim clouds clear A feeling of contentment. The happiness of living in the moment, he noticed Made problems insignificant, worries irrelevant. Made time travel possible, life beautiful."
         di=te.get_emotion(text)
         return render_template('audio.html',d=di)
    
      
