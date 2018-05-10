import requests

URL = 'http://localhost:5000/wave'
SAVE_PATH = 'resource/res.wav'


def download(payload):
    res = requests.get(URL, params=payload)
    with open(SAVE_PATH, 'wb') as output:
        output.write(res.content)


if __name__ == "__main__":
    payload = {}
    download(payload)
