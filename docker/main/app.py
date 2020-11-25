from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
def index():
    # hostname = os.getenv('HOSTNAME') 
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return render_template('index.html', hostname=hostname, local_ip=local_ip)
    #return "<h1 style='color:red'>Hello There!</h1> <BR> FROM <B>{} </B>| {}".format(hostname,local_ip)


if __name__ == "__main__":
    app.run(host='0.0.0.0')