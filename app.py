from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__, template_folder='templates', static_folder='static')
filename = 'brst_cncr_lgreg.pkl'
#model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')


def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])


def predict():
    perimeter_worst = request.form['perimeter_worst']
    radius_worst  = request.form['radius_worst']
    concave_points_mean = request.form['concave_points_mean']
    area_worst = request.form['area_worst']

    pred = model.predict(np.array([[float(perimeter_worst),float(radius_worst),
                                    float(concave_points_mean), float(area_worst)]]))

    result = "not valid"                                
    if pred == 0:
        result = "No Cancer Found"
    else:
        result = "Cancer Present"

    return render_template('index.html', predict=result)

    #return render_template('index.html', predict=str(pred))


if __name__ == '__main__':
    app.run
