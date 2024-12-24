from pydantic import BaseModel, Field

class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., description="Length of the sepal in centimeters")
    sepal_width: float = Field(..., description="Width of the sepal in centimeters")
    petal_length: float = Field(..., description="Length of the petal in centimeters")
    petal_width: float = Field(..., description="Width of the petal in centimeters")