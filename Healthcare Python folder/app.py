from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        
        name = request.form['name']
        age = request.form['age']

       
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        
        print(f"Name: {name}, Age: {age}, File: {file.filename if file else 'No File'}")

        return f"Thank you {name}, your data has been submitted!"

if __name__ == '__main__':
    app.run(debug=True)
