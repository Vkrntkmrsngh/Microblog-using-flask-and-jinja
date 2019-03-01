
from flask import render_template
from app import app

@app.route("/")
@app.route("/index")


def index():
    user={'username':'Vikrant'}
    posts=[
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Portland'
        },
        {
            'author':{'username':'David'},
            'body':'Movie was good'
        }
    ]
    return render_template("index.html",title='Home',user=user,posts=posts)
