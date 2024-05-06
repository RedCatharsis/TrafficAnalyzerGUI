from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    message = get_flashed_messages(with_categories=True)
    return render_template('index.html', message=message)

#test code for start scan button
@app.route('/scan', methods=['POST'])
def scan(): #triggered when button is pressed
    if request.method == 'POST':
        return "Scanning network..."
    else:
        return "Invalid request method"

@app.route('/popup', methods=['POST'])
def popup():
    return render_template('popup.html')

#app.config allows the app.py file to look for the static folder to use the CSS file in webpage
app.config['STATIC_FOLDER'] = 'static'

if __name__ == "__main__":
    app.run(debug=True)