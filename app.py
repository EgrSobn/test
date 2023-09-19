from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def testovoe():

    name = request.args.get('name')
    message = request.args.get('message')

    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80)