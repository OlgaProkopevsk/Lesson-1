from flask import Flask, jsonify, request

from model.twit import Twit

twits = []

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def create_twits():
    '''{"body": "Hello Word", "autor": "@aqague"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['autor'])
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['Get'])
def read_twits():
    return jsonify({'twits': 'twits'})



if __name__=='__main__':
    app.run(debug=True)

