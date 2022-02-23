from flask import Flask

from threading import Thread



app = Flask('')



@app.route('/')

def home():

    return "(yourprefix)copyserver also join team gn - https://dsc.gg/team-gn"



def run():

  app.run(host='0.0.0.0',port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()
