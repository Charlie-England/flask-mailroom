import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor, db

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods = ['GET','POST'])
def create():
    if request.method == "POST":
        db.connect()
        name = request.form['name-input']
        donation_amt = request.form['donation-input']
        Donation.insert(value = donation_amt, donor = Donor.select().where(Donor.name == name)).execute()
        return redirect(url_for('home'))
    else:
        return render_template('create.jinja2')
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

