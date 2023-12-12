from ultralytics import YOLO

# Create a new YOLO model from scratch
# model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('pretrained_model/yolov8x.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
# results = model.train(data='coco.yaml', epochs=3, classes=45)
# results = model.train(data='data/cat.yaml', epochs=300, device="cuda:1")
# results = model.train(data='data/bowl.yaml', batch=16, device="cuda:1")
results = model.train(data='data/bowl.yaml', batch=16)
# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
# results = model('test_images/cat.jpg')

# Export the model to ONNX format
# success = model.export(format='onnx')
