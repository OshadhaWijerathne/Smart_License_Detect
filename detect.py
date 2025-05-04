import glob
from ultralytics import YOLO
import os
import cv2

def detect_one_licence(image_path):
    results = model(image_path)
    results[0].show()

def detect_licence(path, save_path):
    image_paths = glob.glob(f"{path}/*.jpg")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for img_path in image_paths:

        results = model(img_path)
        result_img = results[0].plot()
        result_image_path = os.path.join(save_path, os.path.basename(img_path))
        cv2.imwrite(result_image_path, result_img)
        print(f"Result saved at: {result_image_path}")

if __name__ == "__main__":
    # Load the trained model
    model = YOLO("Trained_Model/my_model_yolo8n.pt")
    path = "test_set"  
    save_path = "results"  
    detect_licence(path, save_path)
