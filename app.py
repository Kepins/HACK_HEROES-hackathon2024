import os.path

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder='templates')


@app.route('/')
def upload_form():
    return render_template('upload_form.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'csvFile' in request.files:
        csv_file = request.files['csvFile']
        # You can process the CSV file here (e.g., save it, read it, etc.)
        return redirect(url_for('main_view'))
    else:
        return 'No file uploaded'


@app.route('/main_view')
def main_view():
    return render_template('main_view.html')


if __name__ == '__main__':
    app.run(debug=True)
