from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

bp = Blueprint('main', __name__)

x = 0

@bp.route('/')
def index():
    #initializeFire() 
    #default_app = firebase_admin.initialize_app()
    

    #db = firestore.client()

    # Consulto la base
    #query = db.collection(u'07-01-2021')

    #flash(query)
    
    return render_template('main.html')

def initializeFire():
    cred = credentials.Certificate('tierra/tierrasur-sa-8bdf08a269f8.json')
    firebase_admin.initialize_app(cred)