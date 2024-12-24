import os
import pickle
import numpy as np
from typing import Union
from schemas.features import IrisFeatures

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

    def predict(self, features: IrisFeatures, return_label: bool = False) -> Union[str, int]:
        """
        Predict the species of an Iris flower.

        Args:
            features (IrisFeatures): The morphological features of the Iris flower.
            return_label (bool): Whether to return species as labels (0, 1, 2) instead of strings.

        Returns:
            Union[str, int]: The predicted species of the Iris flower.
        """
        input_features = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
        scaled_features = self.scaler.transform(input_features)
        prediction = self.model.predict(scaled_features)
        
        if return_label:
            return prediction[0]
        else:
            return SPECIES_MAPPING[prediction[0]]

predictor_service = Predictor()