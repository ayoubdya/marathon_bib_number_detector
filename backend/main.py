from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

from detector import Detector
from config import IMAGES_FOLDER, MODEL_PATH

app = FastAPI()
detector = Detector(MODEL_PATH)

app.mount("/photos", StaticFiles(directory=IMAGES_FOLDER), name="photos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/images")
async def upload_images(files: List[UploadFile] = File(...)):
    new_images = []
    for file in files:
        filename = file.filename
        if filename is None:
            continue
        file_path = os.path.join(IMAGES_FOLDER, filename)
        new_images.append(file_path)
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            contents = await file.read()
            buffer.write(contents)

    result = detector.detect_images(new_images)
    print(result)
    detector.update_data(result)

    return {"message": "Images detected successfully"}


@app.get("/number")
def get_images_by_bib_number(bib_number: str):
    data = detector.load_data()  # number: [image_path]
    matching_images = []
    if data.get(bib_number):
        matching_images = data[bib_number]
    return matching_images  # [image_path]
