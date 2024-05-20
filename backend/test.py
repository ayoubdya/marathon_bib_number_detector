from detector import Detector
import os
from tools import load_dump

# model_path = 'models/best.pt'
# image_paths = os.listdir('photos')
# image_paths = image_paths[10:20]
# folder_path = 'photos'
# image_paths = [os.path.join(folder_path, image_path)
#                for image_path in image_paths]
# print(image_paths)

# detector = Detector(model_path)
# result_dict = detector.detect_images(image_paths)
# detector.dump_results(result_dict)
# dump result glob

result_dict = load_dump()
print(result_dict)
