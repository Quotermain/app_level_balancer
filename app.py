import json
import requests

from flask import Flask, request
from markupsafe import escape
from utils.get_comments import get_comments


app = Flask(__name__)

@app.route('/<video_id>', methods=['GET'])
def retrieve_comments(video_id):
    video_id = str(video_id)
    list_of_comments = get_comments(video_id)
    dict_of_comments = {
        i: value
        for i, value in enumerate(list_of_comments)
    }
    prediction = requests.post(
        'http://192.168.10.21:5000/predict',
        json=dict_of_comments
    )
    return prediction.text

if __name__ == "__main__":
    app.run(host='0.0.0.0')
