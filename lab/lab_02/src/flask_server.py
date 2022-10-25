import os
import subprocess

from flask import Flask, Response, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/upload/'


@app.route('/')
def home():
    files_list = []
    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            files_list.append(file)
    print(files_list)
    return render_template('index.html', files=files_list)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/api/upload', methods=['POST'])
def api_upload():
    # Retrieve the file data. (Includes filename)
    data = request.files['file']

    # Save the input file to a location
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        print('Creating upload directory.')
        os.mkdir(app.config["UPLOAD_FOLDER"])

    # Compute the file paths and save the file to that path.
    path_csv = f'{app.config["UPLOAD_FOLDER"]}/{secure_filename(data.filename)}'
    path_xml = path_csv[:-3] + "xml"
    data.save(path_csv)

    # Convert the file from CSV to XML format.
    subprocess.run([f"cat {path_csv} | csv2 | 2xml > {path_xml}"], shell=True)
    response = Response(render_template('upload.html'))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16080, debug=True)
