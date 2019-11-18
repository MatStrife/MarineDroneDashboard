from flask import Flask, render_template, request
from pusher import Pusher

app = Flask(__name__)
# configure pusher object
pusher = Pusher(
app_id='901141',
key='ebecb475b0e0940aa78d',
secret='9a6a44809b0fdc61a374',
cluster='us2',
ssl=True)
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/orders', methods=['POST'])
def order():
    data = request.form
    pusher.trigger(u'order', u'place', {
        u'units': data['units'],
        u'month' : data['month']
    })
    return "Dados enviados"
@app.route('/message', methods=['POST'])
def message():
    data = request.form
    pusher.trigger(u'message', u'send', {
        u'name': data['name'],
        u'message': data['message']
    })
    return "Mensagem Enviada"
@app.route('/customer', methods=['POST'])
def customer():
    data = request.form
    pusher.trigger(u'customer', u'add', {
        u'type': data['type'],
        u'latitude': data['latitude'],
        u'longitude': data['longitude'],
        u'level': data['level'],
    })
    return "Alerta Enviado"
if __name__ == '__main__':
    app.run(debug=True)