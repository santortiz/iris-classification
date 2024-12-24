import os
import pickle
import numpy as np

from dotenv import load_dotenv

load_dotenv()

SPECIES_MAPPING = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

class Predictor:
    def __init__(self):

        with open(os.getenv('BEST_MODEL_PATH'), "rb") as model_file:
            self.model = pickle.load(model_file)

        with open(os.getenv('SCALER_PATH'), "rb") as scaler_file:
            self.scaler = pickle.load(scaler_file)

    def predict(self, features):
        
        input_features = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
        scaled_features = self.scaler.transform(input_features)
        prediction = self.model.predict(scaled_features)
        species = SPECIES_MAPPING[prediction[0]]

        return species
    

predictor_service = Predictor()