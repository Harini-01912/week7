from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<center>Hello, World!<br><a href='/register'>Register</a></center>"


@app.route('/success/<name>/<roll_no>/<year>')
def success(name, roll_no, year):
    return render_template(
        'success.html',
        name=name,
        roll_no=roll_no,
        year=year
    )


@app.route('/register', methods=['GET'])
def register_get():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll_no = request.form['roll_no']
    year = request.form['year']

    return redirect(
        url_for(
            'success',
            name=name,
            roll_no=roll_no,
            year=year
        )
    )


if __name__ == '__main__':
    import os

    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=debug_mode
    )