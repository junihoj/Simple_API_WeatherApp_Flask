from flask import Flask, render_template, request

from greetings import greet

app = Flask(__name__)

@app.route('/')
def main():
    ip_address = request.headers['X-Forwarded-For']
    return render_template('index.htm', message=greet(ip_address))
    # return "hello"
    
    
#return "hello"

# @app.route('/bye')
# def bye():
#     return "good bye"

@app.route('/weather_app')
def bye():
    # return "hello" + greet(ip_address)


if __name__=='__main__':
    app.run(debug=True)