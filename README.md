# heroku_flask_template

A basic template for deploying a flask app to heroku.

Foundational code from https://github.com/datademofun/heroku-basic-flask

### Setup

1. Create a new Github repo
2. Setup a new heroku app
3. Connect your new heroku app up to the github repo of your newly cloned project
4. Make your changes to this template
5. Push your changes to the master branch of your new repo

~~TODO: this project currently runs using python 2.7 as the project it is being used to build runs on python 2.7. This might change in the future~~

You code will then be picked up by Heroku, and deployed to the app that you configured

You can also choose to deploy your code directly to Heroku (rathern than going to through a github repo) but I prefer having my code changes tracked outside of Heroku, so I'll be sticking with this method.

### Testing Locally

When testing/developing your code it is recommeneded to use a python virtual environment. You can find details on the setup process for for that [here](https://github.com/HaywardPeirce/WoL_server#setup). 

### Deployment

When running in production, use the guincorn web server `gunicorn --bind 0.0.0.0:8000 wsgi` 