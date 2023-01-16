from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__, template_folder='templates', static_folder='static')
filename = 'score.pkl'
#model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')


def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])


def predict():
    reading_score = request.form['reading_score']
    writing_score = request.form['writing_score']
    math_score = request.form['math_score']


    pred = model.predict(np.array([[reading_score, writing_score,
                                    math_score]], dtype=float))

    if pred == 0:
        result = "Group A"
    elif pred ==1:
        result = "Group B"
    elif pred ==2:
        result = "Group C"
    elif pred ==3:
        result = "Group D"
    else:
        result = "Group E"


    #return render_template('index.html', predict=str(pred))
    return render_template('index.html', predict=result)



if __name__ == '__main__':
    app.run
