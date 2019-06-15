# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Response
from datetime import datetime
import subprocess
application = Flask(__name__)

@application.route("/update_site", methods=['POST'])
def index():

    # do something if the request method was POST
    if request.method == 'POST' and request.is_json:
        
        data = request.get_json()
        # print(data)

        subprocess.run('./update_site.sh', shell=True)

        resp = Response(status=200)
        return resp


# @application.route('/')
# def homepage():
#     the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

#     # return """
#     # <h1>Hello heroku</h1>
#     # <p>It is currently {time}.</p>
#     # """.format(time=the_time)

#     return render_template('index.html', the_time = the_time )

if __name__ == '__main__':
    application.run(host='0.0.0.0')

