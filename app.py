#from flask import Flask, render_template
import schedule
#import datetime
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return render_template("index.html")
#    #return 'Hello World !'

#if __name__ == "__main__":
#    app.run(debug=True)

def job():
    print("Hello World")
    
schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
