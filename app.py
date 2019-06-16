# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Response
from datetime import datetime
import subprocess, os
application = Flask(__name__)

@application.route("/update_site", methods=['POST'])
def index():

    # do something if the request method was POST
    if request.method == 'POST' and request.is_json:
        
        data = request.get_json()
        # print(data)

        # if the environment variable for which github branch to pull from has been set
        if 'REPO_BRANCH_FAMILY_TREE' in os.environ:
            print(os.environ['REPO_BRANCH_FAMILY_TREE'])

            # if there are multiple branches in the repo, then which branch was pushed will be referenced in the webhook data under (e.g.) `"ref": "refs/heads/master",`
            if 'ref' in data:
                
                # if the branch that was pushed to was the branch that should trigger a rebuild
                if data['ref'] == ("refs/heads/" + os.environ['REPO_BRANCH_FAMILY_TREE'] ):
                    subprocess.run('./update_site.sh', shell=True)

                else:
                    print("This push was from another branch ")

            # There is only one branch in the repo, so this push must be something that should trigger a rebuild
            else: 
                subprocess.run('./update_site.sh', shell=True)

        else: print("Environment variable `REPO_BRANCH_FAMILY_TREE` not found")

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

