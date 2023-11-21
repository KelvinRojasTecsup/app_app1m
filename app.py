# Importa las bibliotecas necesarias
from flask import Flask, jsonify
import pandas as pd

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Lee los datos desde el archivo ratings.dat
ratings_df = pd.read_csv('ratings.dat', sep='::', engine='python', names=['userId', 'movieId', 'rating', 'rating_timestamp'])

# Ruta para obtener todos los datos de ratings
@app.route('/ratings', methods=['GET'])
def get_ratings():
    # Convierte los datos a un formato JSON y los devuelve
    return jsonify(ratings_df.to_dict(orient='records'))

# Ruta para obtener datos de un usuario específico
@app.route('/ratings/user/<int:user_id>', methods=['GET'])
def get_user_ratings(user_id):
    # Filtra los datos para obtener las clasificaciones del usuario específico
    user_ratings = ratings_df[ratings_df['userId'] == user_id]
    # Convierte los datos a un formato JSON y los devuelve
    return jsonify(user_ratings.to_dict(orient='records'))

# Ruta para obtener datos de una película específica
@app.route('/ratings/movie/<int:movie_id>', methods=['GET'])
def get_movie_ratings(movie_id):
    # Filtra los datos para obtener las clasificaciones de la película específica
    movie_ratings = ratings_df[ratings_df['movieId'] == movie_id]
    # Convierte los datos a un formato JSON y los devuelve
    return jsonify(movie_ratings.to_dict(orient='records'))

# Punto de entrada principal
if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 8080
    app.run(host='0.0.0.0', port=8080)