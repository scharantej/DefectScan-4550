
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

comments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    comment = request.form['comment']
    system = request.form['system']
    comments.append({'comment': comment, 'system': system})
    return redirect(url_for('report'))

@app.route('/report')
def report():
    return render_template('report.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
