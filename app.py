import json

from flask import Flask, request
from markupsafe import escape
from utils.get_comments import get_comments


app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/<video_id>', methods=['GET'])
def retrieve_comments(video_id):
    video_id = str(video_id)
    list_of_comments = get_comments(video_id)
    print(list_of_comments[:4])
    return json.dumps({'comments': list_of_comments})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
