from flask import Flask
from flask import request
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import os
import json
import time
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd

from flask.ext.heroku import Heroku
from flask import jsonify
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

context= {'extra': False, 'items': None, 'fragment': False, 'filename': False}


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spectral_library_07112018v1.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
heroku = Heroku(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
from models import *
db.create_all()



# class PForm(FlaskForm):
#     mz = StringField('precursor_mz', validators=[DataRequired()])
#
#     submit = SubmitField('Submit')
#
#
#
# class CForm(FlaskForm):
#     name = StringField('Compound name', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#
#
#
# class FForm(FlaskForm):
#     name = FloatField('fragment_mz', validators=[DataRequired()])
#     ppm= IntegerField('ppm')
#     submit = SubmitField('Submit')



# @app.route('/fragment')
# def fragment():
#     context['fragment']= True
#
#
#     return render_template(
#         "button2.html",
#         context= context
#     )
#
#
# @app.route('/precursor', methods=['GET', 'POST'])
# def precursor():
#     context['fragment']= True
#
#     form = PForm()
#
#     if form.validate_on_submit():
#         mz = form.mz.data
#         print(mz, file=sys.stderr)

#         return redirect(url_for("table"))
#
#
#     return render_template(
#         "button2.html",
#         context= context, form= form
#     )
#
#
# @app.route('/compound')
# def compound():
#     context['fragment']= False
#     context['precursor']= False
#     context['compound']= True
#     print(context, file=sys.stderr)
#
#     return render_template(
#         "button2.html",
#         context= context
#     )



# @app.route("/")
# def index():
#
#     return render_template(
#         "button2.html",
#         context= context
#     )
#
#
#
@app.route("/", methods=["GET", "POST"])
def index():

    context['mz'] = 279.091
    if request.method == "POST":

        mz = request.form['precursor_mz']
        mz = float(mz)
        context['mz']= mz

    return render_template("button2.html", context= context, mz= context['mz'],  items= context['items'])



@app.route("/<float:mz>", methods=["GET", "POST"])
def cal(mz):
    if request.method == "POST":

        mz = request.form['precursor_mz']
        mz = float(mz)

    results= Library_spectra_meta.query.filter(Library_spectra_meta.precursor_mz >= mz - 0.002, Library_spectra_meta.precursor_mz <= mz + 0.002)
    items = []
    for result in results:
        an_item = dict(id = result.id, precursor_mz= result.precursor_mz, name= result.name, collision_energy = result.collision_energy, retention_time= result.retention_time, mass_accuracy= result.mass_accuracy, mass_error= result.mass_error)
        items.append(an_item)
    context['items']= items
    return render_template("button2.html", context= context, mz= context['mz'], items= context['items'])





@app.route('/view_plot/<int:number>', methods=["GET", "POST"])
def about(number):
    if request.method == "POST":
        return redirect("/", code=303)

    context['extra']= True
    mz1= []
    intensity= []
    plots= Library_Spectra.query.filter(Library_Spectra.library_spectra_meta_id== int(number))
    result = Library_spectra_meta.query.filter(Library_spectra_meta.id == number)
    for r in result:
        name= r.name
        collision_energy= r.collision_energy
    for plot in plots:
        mz1.append(plot.mz)
        intensity.append(plot.i)
    fig = plt.figure()
    plt.bar(mz1, intensity)

    fig.suptitle(f"plot of {name} at {collision_energy}", fontsize=20)
    plt.xlabel('mz', fontsize=18)
    plt.ylabel('relative intensity', fontsize=16)
    filename= str(number) + "plot" + ".png"
    context['filename']= filename
    fig.savefig(os.path.join('static', filename))
    return render_template("button2.html", context= context, mz= context['mz'], items= context['items'], filename= filename)




if __name__ == '__main__':
    app.debug = True
    app.run()
