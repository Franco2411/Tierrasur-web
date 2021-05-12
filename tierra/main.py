from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('main', __name__)

x = 0



@bp.route('/')
def index():
    
    return render_template('main.html')


    