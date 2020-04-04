from app import app
from app import db
from app.models import User, Post
from app import cli

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}

