from flask import Flask, url_for, request, render_template, Response
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello world')


@app.route('/fibonacci')
def US():
    host_name = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    x = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if (host_name == None or fs_port == None or x == None or as_ip == None or as_port == None):
        return Response("Bad request: Missing Parameters", status=400)
    else:
        print(f"{host_name} {fs_port} {x} {as_ip} {as_port}")
        # ask address from AS
        ip_info = {'name': host_name, 'fs_port': fs_port}
        req = requests.get('http://' + as_ip + ':' + as_port, params=ip_info)
        if req.status_code == 404:
            return "404 not found"
        # send request to FS
        ip_address_FS = 'http://' + req.text + ':' + fs_port + '/fibonacci?number=' + x
        print(ip_address_FS)
        req = requests.get(ip_address_FS)
        # output result
        return req.text


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

