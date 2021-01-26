from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main.html')