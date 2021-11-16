from imageai.Detection import VideoObjectDetection
import os

"""
Detects object from pre-recorded video-file.
Outputs the path to the processed video with objects detected.
"""

path_to_model = "./../models/gtsrb.h5"
input_file_path = "./../videos/input/traffic-mini.mp4"
output_file_path = "./../videos/output/traffic_mini_detected_1"

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, path_to_model))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
	input_file_path=os.path.join(execution_path, input_file_path),
	output_file_path=os.path.join(execution_path, output_file_path), 
	frames_per_second=29, 
	log_progress=True
)

print(video_path)