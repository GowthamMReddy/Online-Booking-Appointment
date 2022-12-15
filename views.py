from flask import Flask
from flask import Blueprint,render_template,url_for

views=Blueprint(__name__,"views")

@views.route("/")
def userdashboard():
    return render_template('userdashboard.html', value1='Basic', value2='Standard', value3='Premium')

