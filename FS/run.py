from flask import Flask, request, Response
import requests
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'FS server: Hello world!'

# send UDP message to the server
@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '0.0.0.0'
    dict = {}
    dict['name'] = host_name
    dict['address'] = ip_address
    req = requests.put('http://0.0.0.0:53533', data = dict)
    # registration successful, status 201
    return Response(req.text, status = 201)

@app.route('/fibonacci')
def fibonacci():
    num = request.args.get('number')
    if num.is_integer():
        result = calc_fib(num)
        return Response("the fibo for "+str(num)+" is: "+str(result), status = 200)
    else:
        return Response("bad format", status = 400)



def calc_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

app.run(host='0.0.0.0',
        port=9090,
        debug=True)