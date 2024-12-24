from fastapi import APIRouter, Query
from schemas.features import IrisFeatures
from services.predictor import predictor_service

router = APIRouter()

@router.post(
    "/predict",
    summary="Predict Iris Species",
    description="Predict the species of an Iris flower based on its morphological features."
)
def predict_species(
    features: IrisFeatures,
    return_label: bool = Query(False, description="Return species as labels (0, 1, 2) instead of strings")
) -> dict[str, str | int]:
    """
    Predict the species of an Iris flower.

    Args:
    - **sepal_length**: Length of the sepal in centimeters
    - **sepal_width**: Width of the sepal in centimeters
    - **petal_length**: Length of the petal in centimeters
    - **petal_width**: Width of the petal in centimeters
    - **return_label**: Whether to return species as labels (0, 1, 2) instead of strings

    Returns:
    - **species**: The predicted species of the Iris flower.
    """
    species = predictor_service.predict(features, return_label)
    
    return {"species": species}