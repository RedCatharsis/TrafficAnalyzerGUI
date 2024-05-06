from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

#test code for button
@app.route('/scan', methods=['POST'])  # New route for scan action
def scan():
    
    if request.method == 'POST':
        return "Scanning network..."
    else:
        return "Invalid request method"

if __name__ == "__main__":
    app.run(debug=True)