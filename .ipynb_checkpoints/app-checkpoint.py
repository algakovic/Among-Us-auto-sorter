import os
from flask import Flask, render_template, request, redirect, url_for, abort
from Autosorter import among_us_lobby_sorter
from werkzeug.utils import secure_filename 

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.txt']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def upload_file():
    for uploaded_file in request.files.getlist('file'):
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            
 
    lobbies = among_us_lobby_sorter()
    os.system('rm uploads/admins.txt')
    os.system('rm uploads/participants.txt')
    os.system('rm uploads/standby.txt')
    return render_template('results.html', lobbies=lobbies)
    
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)