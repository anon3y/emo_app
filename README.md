<h1>Emotion classification using Audio</h1>

<b> Function </b>

The Flask app uses random forest in the backend to a user uploaded .wav file and predicts emotion of the audio file


<b> Data Set Used to train the model </b>

<li>Speech file (Audio_Speech_Actors_01-24.zip, 215 MB) contains 1440 files: 60 trials per actor x 24 actors = 1440.</li>
<li>Song file (Audio_Song_Actors_01-24.zip, 198 MB) contains 1012 files: 44 trials per actor x 23 actors = 1012.</li>

<b> Complete Data Set        : <a href="https://zenodo.org/record/1188976#.XSF23-hKiM9">RAVDESS</a> </b>


<b>File naming convention</b>

Each of the 7356 RAVDESS files has a unique filename. The filename consists of a 7-part numerical identifier (e.g., 02-01-06-01-02-01-12.mp4). These identifiers define the stimulus characteristics: 

Filename identifiers 

Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
Vocal channel (01 = speech, 02 = song).
Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
Repetition (01 = 1st repetition, 02 = 2nd repetition).
Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

Filename example: 02-01-06-01-02-01-12.mp4 

Video-only (02)
Speech (01)
Fearful (06)
Normal intensity (01)
Statement "dogs" (02)
1st Repetition (01)
12th Actor (12)
Female, as the actor ID number is even.


<h1> Flask App </h1>

<li>hosted on <a href="https://www.heroku.com"> Heroku </a></li>
<li>Link to the app : <a href="https://emo-app.herokuapp.com/">App</a></li>
<li>Versions and Frameworks used are in requirements.txt</li>



<h3>Info!</h3>
  The app only takes .wav files as input no larger than 5MB








