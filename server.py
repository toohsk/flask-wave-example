from flask import Flask, Response, stream_with_context

app = Flask(__name__)
BUFFER_SIZE = 1024
WAVE_FILE = 'resource/song.wav'


@app.route('/wave')
def wave_res():

    def generate():
        with open(WAVE_FILE, 'rb') as wav_f:
            data = wav_f.read(BUFFER_SIZE)
            while data:
                yield data
                data = wav_f.read(BUFFER_SIZE)

    return Response(stream_with_context(generate()), mimetype="audio/wav")


if __name__ == "__main__":
    app.run(debug=True)
    # if you want to test api out from localhost, use below
    # app.run(debug=True, host='0.0.0.0', port=8080)
