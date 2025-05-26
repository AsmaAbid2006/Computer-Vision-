from ultralytics import YOLO
model=YOLO('yolov8m-pose.pt')
results=model(source='Task7/videos/video.mp4',show=True, conf=0.3,save=True)