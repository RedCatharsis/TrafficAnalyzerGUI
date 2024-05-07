from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

#popup
@app.route('/popup', methods=['POST'])
def popup(text): #include text for popup to display
    if request.method == 'POST':
        return render_template('popup.html', custom_text=text)
    else:
        return 'Invalid request'
    
#when start scan button is pressed this is referenced
#this forwards to another webpage where scan results are shown
@app.route('/result', methods=['POST'])
def result():

    #assign previous incidents to the list
    #all the generated incident report files can be accesed and their names be used to create entires 
    #currently loads html files from templates folder. change folder name and file type

    foldername = "templates"
    filetype = ".html"

    files = []
    if os.path.isdir(foldername):
        for filename in os.listdir(foldername):
            if filename.endswith(filetype):
                files.append({'value': filename, 'label': filename.removesuffix(filetype)})
    
    if request.method == 'POST':
        #any code that is run when start scan button is pressed goes in there before the return
        return render_template('result.html', incidents=files)
    else:
        return 'Invalid request'   
    
#when an incident is selected in the incidents list this code is excecuted
@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        data = request.json
        filename = data.get('filename')
        
        #file can be accessed using filename to look up the file in folder

        return result()
    else:
        return 'Invalid request'  

#app.config allows the app.py file to look for the static folder to use the CSS file in webpage
app.config['STATIC_FOLDER'] = 'static'

if __name__ == "__main__":
    app.run(debug=True)