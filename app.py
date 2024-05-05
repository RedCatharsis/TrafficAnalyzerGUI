from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('base.html')
    return render_template('index.html') 

@app.route('/download_button')
def download_button():
    return render_template('download_button.html')

@app.route('/download_output')
def download_output():
    return render_template('download_output.html')

@app.route('/dropdown_list')
def dropdown_list():
    return render_template('dropdown_list.html')

if __name__ == "__main__":
    app.run(debug=True)