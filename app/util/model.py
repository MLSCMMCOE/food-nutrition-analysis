from transformers import pipeline
import torch
from PIL import Image

model_name = "indian_food_image_detection"

class Model:
    def __init__(self):
        self.model = pipeline('image-classification',model=model_name,device=0 if torch.cuda.is_available() else -1)
      
    def predict(self, image: Image):
        prediction = self.model(image)
        return prediction

