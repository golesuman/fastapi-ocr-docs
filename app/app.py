
from fastapi import FastAPI
from fastapi import File, UploadFile
# import cv2
import uvicorn
import io
from .utils import predict
from PIL import Image


app = FastAPI()


@app.get("/")
async def home():
    return {"message" : "new message"}

@app.post("/upload_file/")
async def predict_words_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "image must be jpg or png format"
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    prediction = predict(image)
    return prediction
 
    