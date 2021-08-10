from flask import Flask, render_template, request

from greetings import greet

app = Flask(__name__)

@app.route('/')
def main():
    # ip_address = request.headers['X-Real-IP']
    ip_address = None
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_address = request.environ['REMOTE_ADDR']
    else:
       ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    return render_template('index.htm', message= ip_address)
    
if __name__=='__main__':
    app.run(debug=True)