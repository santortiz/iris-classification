from fastapi import APIRouter
from schemas.features import IrisFeatures
from services.model import predictor_service

router = APIRouter()

@router.post("/predict")
def predict_species(features: IrisFeatures):

    species = predictor_service.predict(features)
    
    return {"species": species}
