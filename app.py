import csv
import io

import pandas
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def upload_csv():
    return render_template('upload_form.html')


@app.route('/path/', methods=['POST'])
def paths():
    paths = []
    map_path = ''
    if request.method == 'POST':
        if 'file' in request.files:
            csv_file = request.files['file']
            stream = io.StringIO(csv_file.stream.read().decode("UTF-8"), newline="")
            csv_data = pandas.read_csv(stream)

            return redirect("/paths/" + str(id))
    return render_template('upload_form.html')


@app.route('/paths/<id>', methods=['GET'])
def pathsid(id):
    paths = []
    map_path = ''

    return render_template('index.html', map_path=map_path, paths=paths)


if __name__ == '__main__':
    app.run(debug=True)

