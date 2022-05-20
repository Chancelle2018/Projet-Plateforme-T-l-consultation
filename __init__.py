# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:28:58 2021

@author: chane
"""

from flask import Flask
app= Flask(__name__)
app.secret_key='toto'
from app import views