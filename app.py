import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Membaca file model
with open('storage/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Membaca file CountVectorizer
with open('storage/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Membaca data dari file CSV
dataframe = pd.read_csv('storage/data_diagnose.csv')

@app.route('/predict', methods=['POST'])
def predict():
    # Menerima input gejala dari permintaan POST
    gejala1 = request.json['gejala1']
    gejala2 = request.json['gejala2']
    gejala3 = request.json['gejala3']

    # Melakukan vectorization pada gejala input
    X_input = vectorizer.transform([' '.join([gejala1, gejala2, gejala3])])

    # Melakukan prediksi menggunakan model
    hasil_prediksi = model.predict(X_input)
    diagnosis = hasil_prediksi[0]

    # Mengambil pengertian diagnosis dan cara mengatasinya dari dataframe
    pengertian = dataframe.loc[dataframe['diagnosis'] == diagnosis, 'penjelasan'].values[0]
    cara_mengatasi = dataframe.loc[dataframe['diagnosis'] == diagnosis, 'solusi'].values[0]

    # Mengembalikan hasil prediksi, pengertian, dan cara mengatasi dalam bentuk JSON
    response = {
        'diagnosis': diagnosis,
        'pengertian': pengertian,
        'solusi': cara_mengatasi
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
