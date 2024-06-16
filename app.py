from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/core-banking')
def core_banking():
    return render_template('core-banking.html')

@app.route('/bpm-workflows')
def bpm_workflows():
    return render_template('bpm-workflows.html')

@app.route('/balador-queuing')
def balador_queuing():
    return render_template('balador-queuing.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()