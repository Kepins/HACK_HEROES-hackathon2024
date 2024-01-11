import csv
import io

import pandas
from flask import Flask, render_template, request, redirect

from models import Tour
from session import db

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

            tour = Tour()
            db.add(tour)
            db.commit()

            return redirect("/paths/" + str(tour.id))
    return render_template('upload_form.html')


@app.route('/paths/<id>', methods=['GET'])
def pathsid(id):
    tour = db.query(Tour).filter(Tour.id == id)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

