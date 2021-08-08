# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))


# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python v' + sys.version.split()[0] + '\n'
#     response = '\n'.join([message, version])
#     return [response.encode()]


import os
import sys
from flask import Flask, render_template , redirect , url_for , jsonify , request
from flask_mail import Message , Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = '123giadinh123giadinh'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] =  False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ln840098@gmail.com'
app.config['MAIL_PASSWORD'] = '123giadinh'
app.config['MAIL_DEBUG'] = True

mail = Mail()

mail.init_app(app)


@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/Services')
def services():
    return render_template('services.html')

@app.route('/Industries')
def industries():
    return render_template('indus.html')


@app.route('/Equipment')
def equipment():
    return render_template('equipment.html')


@app.route('/Location')
def location():
    return render_template('location.html')

@app.route('/Company' , methods = ['GET' , 'POST'])
def company():
    if request.method == 'POST':
        
        messages_format = {}
    
        messages_format['name'] = request.form['name']
        messages_format['email'] = request.form['email']
        messages_format['messages'] = request.form['messages']
        
        msg = Message("Sales Inquiry" , sender = "V3 Robot" , recipients=["Sales@v3mfg.com"])        
        
        msg.body = """ Hello there , 
        Name : {}
        Email: {}
        Messages:{}
        """.format(messages_format['name'] , messages_format['email'] , messages_format['messages'])
        
        if True:
        
            mail.send(msg)
            
            return jsonify({'success':'True'})
    
    return render_template('company.html')


#####################################
if __name__ ==  '__main__':
    app.run(debug=True, host='127.0.0.1' , port=5000)