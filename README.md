# Family Tree Site Builder

### Setup

1. Install Python 3.6+. For debian-based systems: `sudo apt-get install python3.6 pip3 pip`
2. Install all the needed python libraries `pip install -r requirements.txt`
3. Install the Firebase CLI tools `npm install -g firebase-tools`
4. Login to Firebase and retirve the refresh token that will be used to authenticate with Firebase: https://github.com/firebase/firebase-tools#using-with-ci-systems
3. Setup environment variables. Edit `nano ~/.bashrc` and then refresh the environment variables `source ~/.bashrc` with the following info:
```export REPO_BRANCH_FAMILY_TREE=master
export REPO_BRANCH_P2G=python3
export FIREBASE_TOKEN=whateveryourtokenis
PATH=~/.local/bin/:$PATH``` (Included to help with npm: http://michaelb.org/the-right-way-to-do-global-npm-install-without-sudo/)

### Testing Locally

When testing/developing your code it is recommeneded to use a python virtual environment. You can find details on the setup process for for that [here](https://github.com/HaywardPeirce/WoL_server#setup).

The app can then be run by calling `python app.py` within the virtual environment

### Deployment

When running in production, use the guincorn web server `gunicorn --bind 0.0.0.0:8000 wsgi` 

TODO: include CLI option for pushing updates to firebase


#### API-based Firebase setup (TODO)
Setup firebase: https://firebase.google.com/docs/cli#install_the_firebase_cli

1. Setup a firebase project
2. Enable the [firebase hosting API](https://firebase.google.com/docs/hosting/api-deploy) in the google API tools
3. 

setup `gedcom2html/generated` as the Firebase hosting directory to be uploaded
`firebase deploy`

https://firebase.google.com/docs/hosting/api-deploy

pip install --upgrade oauth2client
pip install --upgrade google-api-python-client






You can also choose to deploy your code directly to Heroku (rathern than going to through a github repo) but I prefer having my code changes tracked outside of Heroku, so I'll be sticking with this method.

