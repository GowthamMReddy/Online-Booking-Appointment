from flask import Flask
from flask import Blueprint,render_template,url_for

views=Blueprint(__name__,"views")

@views.route("/")
def userdashboard():
    return render_template('userdashboard.html', value1='Crime Issues', value2='Property litigation', value3='Marital Issues', value4='Agreements & Notary',lawyerName='Venkatrao Seelam',lawyerAddrs='1509, Headford Terrace, Ireland',lawyerContact='+353 98765432')

    