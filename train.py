from ultralytics import YOLO

if __name__ == "__main__":

    # Load a pretrained model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="custom.yaml",
        epochs=50,
        imgsz=640,
        batch=16
    )