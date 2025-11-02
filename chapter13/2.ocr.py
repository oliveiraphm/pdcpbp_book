import os
import pandas as pd
from paddleocr import PaddleOCR
import cv2
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang='en')

folder_path = 'chapter13/images'
supported_extensions = ('.png', '.jpg', '.jpeg')

image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
               if f.lower().endswith(supported_extensions)]

df = pd.DataFrame(columns=['Image Path', 'Extracted Text'])

def process_image(image_path):
    result = ocr.ocr(image_path)

    extracted_text = ""
    for page in result:
        for line in page:
            box = [[int(float(coord)) for coord in point] for point in line[0]]
            text = line[1][0]
            extracted_text += text + " "

    print(f"Extracted Text from {os.path.basename(image_path)}:\n{extracted_text}\n")

    image = cv2.imread(image_path)
    for page in result:
        for line in page:
            box = [[int(float(coord)) for coord in point] for point in line[0]]
            text = line[1][0]
            cv2.polylines(image, [np.array(box)], isClosed=True, color=(0,255,0), thickness=2)
            cv2.putText(image, text, (box[0][0], box[0][1]-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imwrite(f"{os.path.splitext(image_path)[0]}_ocr.jpg", image)
    df.loc[len(df)] = [image_path, extracted_text]

for image_path in image_paths:
    process_image(image_path)

print(df)
df.to_csv('extracted_texts.csv', index=False)