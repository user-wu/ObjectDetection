from ultralytics import YOLO

# Create a new YOLO model from scratch
# model = YOLO('yolov8n.yaml')
# model = YOLO('yolov8n.pt')
model = YOLO('./runs/detect/train28/weights/best.pt')

# Perform object detection on an image using the model
results = model('test_images',save=True)
# results = model('test_images/3.jpg',save=True)

# Export the model to ONNX format
# success = model.export(format='onnx')
