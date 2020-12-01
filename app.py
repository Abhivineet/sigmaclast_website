import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage

UPLOAD_FOLDER = 'data/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'zip'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


if __name__ == '__main__':
    app.debug =True
    app.run()

# @app.route('/', methods=['GET', 'POST'])   
# def home():
#     return app.send_static_file("index.html") 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/', methods=['GET', 'POST'])

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        print('here')
        if request.form:
            # print(request.form)
            # msg['From'] = request.form['email']
            
            # msg.set_content(request.form['message'] + '\n\n' + request.form['name'] + '\n' + request.form['phone'])
            with open("messages.txt", "a") as f:
                f.write(request.form['name'] + '\t' + request.form['phone'] + '\t' + request.form['email'] + '\t' + request.form['message'])
            
        if request.files:        
                                                                        # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                                                                        # return redirect(request.url)
            file = request.files['file']
            print(type(file))
                                                                        # if user does not select file, browser also
                                                                        # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                # return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # return redirect(url_for('upload_file', filename=filename))

    return app.send_static_file("index.html") 