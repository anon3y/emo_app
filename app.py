
from flask import Flask, render_template, request
import librosa as lr
import pickle
import numpy as np
import librosa.feature



model = pickle.load(open('model.pkl', 'rb'))


def mffc_extract(file):
    audio, sfreq = lr.load(file, sr=48000,offset=0.5,duration=3.5)
    mfccs = np.mean(librosa.feature.mfcc(audio, sr=sfreq).T, axis=0)
    return mfccs.reshape(-1, 20)


def convert_emo(value):
    my_dict={0:'angry', 1:'calm',2: 'fearful', 3:'happy', 4:'sad', 5:'surprised'}
    return my_dict.get(value)



app = Flask(__name__)
app.secret_key = "super secret key"
app.config['MAX_CONTENT_LENGTH'] = 5*1024*1024


@app.route('/')
def upload():
    return render_template('index1.html')


@app.route('/upload', methods=['POST'])
def uploader():
    '''
    check if the action is post and there is a file present
    then the function retruns the index template and invokes the functions
    to predict emotions

    '''
    if request.method == 'POST':
            f = request.files['file']
            if f.filename!='':
                mfcc = mffc_extract(f)
                return render_template('index1.html',prediction_text=f'your emotion is {convert_emo(model.predict(mfcc)[0])}')
            else:
                return render_template('index.html', warning_text=f'FILE NOT UPLOADED')


if __name__ == "__main__":
    app.debug = True
    app.run()
