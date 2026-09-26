from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # creating instance and naming it as app


@app.route('/')  # @ shows how it should execute the function hello_world() when the user visits the root URL
def hello_world():
    # returning a string that will be displayed in the browser
    return "<center>Hello, World!<br><a href='/register'>Register</a></center>"


@app.route('/success/<name>/<roll_no>/<year>')
def success(name, roll_no, year):
    # rendering the template and passing the values to it
    return render_template('success.html', name=name, roll_no=roll_no, year=year)


@app.route('/register', methods=['GET'])
def register_get():
    return render_template('register.html')


@app.route('/register', methods=['POST']) 
def register():
    name = request.form['name']
    roll_no = request.form['roll_no']
    year = request.form['year']
    return redirect(url_for('success', name=name, roll_no=roll_no, year=year))


if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)