from detector import Detector
import os
from tools import load_dump

model_path = 'models/best.pt'
image_paths = os.listdir('photos')
image_paths = image_paths[10:20]
folder_path = 'photos'
image_paths = [os.path.join(folder_path, image_path)
               for image_path in image_paths]
print(image_paths)

detector = Detector(model_path)
result_dict = detector.detect_images(image_paths)
detector.dump_results(result_dict)

result_dict = load_dump()
print(result_dict)

a = {'11': ['photos/331512766_1195563187761595_2292882292157838148_n.jpg'], '1635': ['photos/331521467_1410170939519911_2223349643195327815_n.jpg'], '1009': ['photos/331521467_1410170939519911_2223349643195327815_n.jpg'], '7071': ['photos/331521467_1410170939519911_2223349643195327815_n.jpg'], '81': ['photos/331783711_680425600502616_2891206310196481997_n.jpg'], '707': ['photos/331783711_680425600502616_2891206310196481997_n.jpg'],
     '82': ['photos/331783711_680425600502616_2891206310196481997_n.jpg'], '156': ['photos/331502925_1249878729297901_3819254621682315928_n.jpg'], '621': ['photos/331501090_524561539816330_8640549082767964486_n.jpg'], '1354': ['photos/331501090_524561539816330_8640549082767964486_n.jpg'], '6608': ['photos/331501090_524561539816330_8640549082767964486_n.jpg'], '327': ['photos/331521149_504026778607643_4583723625879267542_n.jpg']}
