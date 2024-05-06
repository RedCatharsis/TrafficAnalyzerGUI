from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    message = get_flashed_messages(with_categories=True)
    return render_template('index.html', message=message)

#test code for button
@app.route('/scan', methods=['POST'])
def scan():
    if request.method == 'POST':
        return "Scanning network..."
    else:
        return "Invalid request method"

@app.route('/downloadButton', methods=['POST'])
def show_popup():
    flash('This is a popup message!', 'downloading file...') 
    return redirect(url_for('index'))  # Redirect back to the index page

if __name__ == "__main__":
    app.run(debug=True)