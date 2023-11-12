import os
from io import BytesIO
import base64
from flask import Flask, render_template
from flask import Flask, request, Response
from gtts import gTTS
import socket

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def hello_world():

    text = '안녕하세요. 인공지능 로봇 David입니다.'

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)
    encoded_audio_data = base64.b64encode(fp.getvalue())

    if app.debug:
        hostname='컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname=' '

    # return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생
    return render_template('index.html', image_file="david.jpg", audiodata=encoded_audio_data.decode('utf-8'), computername=hostname)

@app.route("/menu")
def menu():
    return render_template('menu.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0', 80)
