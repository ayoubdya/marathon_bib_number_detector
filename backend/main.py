from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from tools import load_dump
from detector import Detector

model_path = "models/best.pt"

app = FastAPI()
data = load_dump()  # number: [image_path]
images = []
detector = Detector(model_path)
# In-memory storage for images and bib numbers

app.mount("/photos", StaticFiles(directory="photos"), name="photos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/images")
async def upload_images(files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        print(contents)
        images.append(contents)
    print(images)
    return {"message": "Images uploaded successfully"}


@app.get("/number")
def get_images_by_bib_number(bib_number: str):
    matching_images = []
    # bib_number = int(bib_number)  # type: ignore
    if data.get(bib_number):
        matching_images = data[bib_number]
    return matching_images  # [image_path]
