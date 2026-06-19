from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_object(image_path):

    results = model(image_path)

    names = model.names

    for result in results:

        boxes = result.boxes

        if len(boxes) > 0:

            cls = int(boxes[0].cls)

            conf = float(boxes[0].conf)

            return {
                "object": names[cls],
                "confidence": round(conf,2)
            }

    return {
        "object": None,
        "confidence": 0
    }