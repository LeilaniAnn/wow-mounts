
import os
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)
api_key = os.environ.get('api_key')


@app.route('/', methods=['GET'])
def home():

    if request.method == 'GET':
        r = requests.get("https://us.api.battle.net/wow/mount/?locale=en_US&apikey="+ api_key)
        data = r.json()
        entries = data['mounts']
        return render_template('index.html', entries=entries)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

