# import os
#
# from flask import Flask, render_template, request, url_for, redirect
#
# app = Flask(__name__, template_folder='templates')
#
#
# @app.route('/')
# def main_view():
#     image_path = request.args.get('image_path')
#     if not image_path:
#         image_path = r'/home/ola/HACK_HEROES-hackathon2024/TASK-FILES/RysunekTechnicznyMagazynuA4-1.png'
#     return render_template('main_view.html', image_path=image_path)
#
#
# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'csvFile' in request.files:
#         csv_file = request.files['csvFile']
#         # calculate path
#         image_path = r'/home/ola/HACK_HEROES-hackathon2024/TASK-FILES/RysunekTechnicznyMagazynuA4-1.png'
#         return redirect(url_for('main_view', image_path=image_path))
#     else:
#         return 'No file uploaded'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<id>', methods=['GET', 'POST'])
def index():
    paths = []

    if request.method == 'POST':
        if 'csvFile' in request.files:
            csv_file = request.files['csvFile']
            # calculate path

            map_path = 'static/RysunekTechnicznyMagazynuA4-1.png'
            paths = ['path1', 'path2']
            paths['trace1'] =
        # powiązanie ścieżka do pliku z trasą jaka trasa to jest

    return render_template('index.html', map_path=map_path, paths=paths)


if __name__ == '__main__':
    app.run(debug=True)

