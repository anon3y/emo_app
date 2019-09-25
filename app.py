import sys
from unittest.mock import MagicMock
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

MOCK_MODULES = ['libsndfile-dev']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
from flask import Flask, render_template, request
import librosa as lr
import pickle
import numpy as np
import librosa.feature



class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

model = pickle.load(open('model.pkl', 'rb'))


def mffc_extract(file):
    audio, sfreq = lr.load(file, sr=48000)
    mfccs = np.mean(librosa.feature.mfcc(audio, sr=sfreq).T, axis=0)
    return mfccs.reshape(-1, 20)


def convert_emo(value):
    my_dict={0:'angry', 1:'calm',2: 'fearful', 3:'happy', 4:'sad', 5:'surprised'}
    return my_dict.get(value)

print(convert_emo(4))

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def upload():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        # flash(f'{f.filename}')
        mfcc = mffc_extract(f)

        return render_template('index.html',prediction_text=f'your emotion is {convert_emo(model.predict(mfcc)[0])}')
        # return f'{f.filename}'


if __name__ == "__main__":
    app.debug = True
    app.run()
