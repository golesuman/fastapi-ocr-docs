
from fastapi import FastAPI
from fastapi import File, UploadFile
# import cv2
from utils import predict


app = FastAPI()
@app.route("/files/", methods=["POST", "GET"])
async def predict_words_api(file:UploadFile = File()):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "image must be jpg or png format"
    # image = cv2.imread(await file.read())
    prediction = predict(await file.read())
    return prediction