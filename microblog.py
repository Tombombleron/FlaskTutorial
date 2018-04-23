# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:04:50 2018

@author: Robert
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User' : User, 'Post' : Post}