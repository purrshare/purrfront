from flask import Flask, render_template
instanceBackendURL = "http://backend.dateien.link:8080/v1/files/"
instanceName = "PurrShare"

app = Flask(__name__)

@app.route('/')
def info():
    return render_template('index.html', instanceBackendURL=instanceBackendURL, instanceName=instanceName)

if __name__ == '__main__':
    app.run(debug=False)