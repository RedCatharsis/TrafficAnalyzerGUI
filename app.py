from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

#popup
@app.route('/popup', methods=['POST'])
def popup(text):
    if request.method == 'POST':
        return render_template('popup.html', custom_text=text)
    else:
        return 'Invalid request'
    
#when start scan button is pressed this is referenced
#this forwards to another webpage where scan results are shown
@app.route('/result', methods=['POST'])
def result():

    #assign previous incidents to the list
    incidents = [
        {'value': 'incident one', 'label': 'incident one | 11/4/2024'},
        {'value': 'incident two', 'label': 'incident two | 12/4/2024'},
        {'value': 'incident three', 'label': 'incident three | 13/4/2024'},
        {'value': 'incident four', 'label': 'incident four | 14/4/2024'},
        {'value': 'incident five', 'label': 'incident five | 15/4/2024'},
        {'value': 'incident six', 'label': 'incident six | 16/4/2024'}
    ]
    if request.method == 'POST':
        return render_template('result.html', incidents=incidents)
    else:
        return 'Invalid request'


#app.config allows the app.py file to look for the static folder to use the CSS file in webpage
app.config['STATIC_FOLDER'] = 'static'

if __name__ == "__main__":
    app.run(debug=True)