from flask import Flask, render_template, request
from preprocess import *

app = Flask(__name__, template_folder='templates')

model_path = './deploy/model/model.h5'

model = tf.keras.models.load_model(model_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        input_text = str(request.form.get('inputtext'))
        text = text_padded_seq(input_text)
        
        prediction = model.predict(text)
        acc = prediction[0][0]
        
        if acc > 0.5:
            label = 'Positif'
            return render_template('index.html', prediction=label)
        elif acc < 0.5:
            label = 'Negatif'
            return render_template('index.html', prediction=label)

app.run(debug=True)
