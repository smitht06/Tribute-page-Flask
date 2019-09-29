"""
Anthony Smith
SDEV 300
Lab 6
Flask App
"""
#import statments 
import datetime
from flask import Flask, render_template
app = Flask(__name__)

#run server at domain/home and /
@app.route('/home')
@app.route('/')
def helloIndex():
 return render_template('home.html')+str(datetime.datetime.utcnow()-datetime.timedelta(hours=4))
 
#run app
if __name__ == '__main__':
 app.run(host='0.0.0.0', port= 8080)
