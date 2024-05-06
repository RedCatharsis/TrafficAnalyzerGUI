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

#popup
@app.route('/popup', methods=['POST'])
def popup():
    if request.method == 'POST':
        custom_text = "random text :3" #use this variable to modify popup text
        return render_template('popup.html', custom_text=custom_text)
    else:
        return 'Invalid request'

#app.config allows the app.py file to look for the static folder to use the CSS file in webpage
app.config['STATIC_FOLDER'] = 'static'

if __name__ == "__main__":
    app.run(debug=True)