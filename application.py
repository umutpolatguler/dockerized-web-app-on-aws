from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css', filename)

@app.route('/scss/<path:filename>')
def scss(filename):
    return send_from_directory('static/scss', filename)

@app.route('/lib/<path:filename>')
def lib(filename):
    return send_from_directory('static/lib', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('static/js', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

