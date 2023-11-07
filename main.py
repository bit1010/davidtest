import os
from io import BytesIO
import base64
from flask import Flask, render_template
from flask import Flask, request, Response
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def hello_world():

    text = '안녕하세요. 인공지능 로봇 David입니다. 무엇을 도와드릴까요?'

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)
    encoded_audio_data = base64.b64encode(fp.getvalue())

    return render_template('index.html', image_file="david.jpg", audiodata=encoded_audio_data.decode('utf-8'))

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0', 80)
