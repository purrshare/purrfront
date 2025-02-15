from flask import Flask, render_template
# use none for hidden or block for show
guestMode = "none"
instanceBackendURL = "http://backend.dateien.link:8080/v1/files/"
instanceName = "PurrShare"

app = Flask(__name__)

@app.route('/')
def info():
    return render_template('index.html', guestMode=guestMode, instanceBackendURL=instanceBackendURL, instanceName=instanceName)

if __name__ == '__main__':
    app.run(debug=False)