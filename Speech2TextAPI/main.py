from app import create_app
import base64
from flask import request, jsonify
from app.speech_to_text import sample_recognize_job

app = create_app()

@app.route('/', methods=['POST'])
def speech_to_text():
    wav_bytes =  base64.b64decode(request.form['bytes'])
    text = sample_recognize_job(wav_bytes)
    json = {
        'response':text
    }
    return jsonify(**json)


if __name__ == '__main__':
    app.run()