from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    message = get_flashed_messages(with_categories=True)
    return render_template('index.html')

#popup
@app.route('/popup', methods=['POST'])
def popup(text):
    if request.method == 'POST':
        return render_template('popup.html', custom_text=text)
    else:
        return 'Invalid request'

#app.config allows the app.py file to look for the static folder to use the CSS file in webpage
app.config['STATIC_FOLDER'] = 'static'

if __name__ == "__main__":
    app.run(debug=True)