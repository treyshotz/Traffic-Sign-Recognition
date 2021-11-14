from imageai.Detection import VideoObjectDetection
import os
import cv2


"""
Detects object from live video capture (camera).
Outputs the path to the processed video with objects detected.

Requires the manual interruption of the program to stop the detection process.
"""

execution_path = os.getcwd()

camera = cv2.VideoCapture(0) 

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
	camera_input=camera,
	output_file_path=os.path.join(execution_path, "camera_detected_1"), 
	frames_per_second=29, 
	log_progress=True
)

print(video_path)
