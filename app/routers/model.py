from fastapi import APIRouter
# import data model
from fastapi import Request
from PIL import Image
from app.util.model import Model
from pydantic import BaseModel
from app.util.nutrition import Nutrition

router = APIRouter()

model = Model()
nutrition = Nutrition("app/data/indian_food_nutrition_updated.csv")


class PredictionResponse(BaseModel):
    prediction: dict
    nutrition: dict



@router.post("/predict")
async def predict(request: Request):
    # extract image data from request
    data = await request.form()
    image = data["file"]
    # convert image to tensor
    image = Image.open(image.file).convert("RGB")
    # get prediction
    prediction = model.predict(image)

    if prediction[0] is None:
        return {"error": "No food item detected in the image"}

    food_item = prediction[0]["label"]

    nutri = nutrition.get_nutrition(food_item.lower())

    if nutri is None:
        return {"error": "Nutrition data not found for the food item detected"}

    return PredictionResponse(prediction=prediction[0], nutrition=nutri)
    
