
from flask import Flask, render_template, request
import librosa as lr
import pickle
import numpy as np
import librosa.feature
import logging
import model_u
logging.basicConfig(filename='log.txt',level=logging.DEBUG)





def mffc_extract(file):
    '''
    return an array

    calculates mean of mfcc's from the audio file, and returns the reshaped array
    '''
    audio, fr = lr.load(file,sr=None,offset=0.1,duration=4)
    logging.debug(f'audio array of the input file is {audio.shape} and sample rate  is {fr}')
    mfccs = np.mean(librosa.feature.mfcc(audio, sr=fr).T, axis=0)
    logging.debug(f'shape of mffcs is {mfccs.shape}')
    logging.debug(f' reshape mfccs is {mfccs.reshape(-1,20)}')
    return mfccs.reshape(-1, 20)


def convert_emo(value):
    '''
    returns the value for each key, the key being the prediction
    '''
    logging.debug(f'the value is {value}')
    my_dict={0:'angry', 1:'calm',2:'disgust',3: 'fearful', 4:'happy', 5:'neutral', 6:'sad',7:'surprised'}
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
                logging.debug(f'the return value from function is{mfcc}')
                model = pickle.load(open('modelu.pkl', 'rb'))
                logging.debug(f'the prediction value is {model.predict(mfcc)}')
                return render_template('index1.html',prediction_text=f'your emotion is {convert_emo(model.predict(model_u.scaler.transform(mfcc))[0])}')
            else:
                return render_template('index.html', warning_text=f'FILE NOT UPLOADED')




if __name__ == "__main__":
    app.debug = True
    app.run()

