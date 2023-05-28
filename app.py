import os
import joblib
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import datetime
import json
app = Flask(__name__)


# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET",'POST'])
def index():
    classifier = joblib.load('./model.pkl')
    predicciones2 = classifier.predict(steps=57)

    base = datetime.date.today()
    dateDict  ={}
    for x in range(0, 5):
        day = base - datetime.timedelta(days=x)
        dateDict[day.strftime('%A')] =predicciones2[str(day)]
    return json.dumps(dateDict)




if __name__ == '__main__':
   app.run()
