
## 반달커피 홈페이지

Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"
https://반달곰 커피 "Go google"

오디오 출력 소스코드
```python
lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)
    encoded_audio_data = base64.b64encode(fp.getvalue())
