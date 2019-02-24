#TODO - implement python server for heroku deployment

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

#database schema
#username / reference existence + check for demo
#top 20 topics 
#time stored, update after a minimum of two weeks

#future todo- graph?