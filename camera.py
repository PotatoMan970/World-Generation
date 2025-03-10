import ursina.prefabs.video_recorder as record
import time
class rec:
    def __init__(self, duration):
        self.cam=record.VideoRecorder(duration, time.time(), fps=120)

    def start_Recording(self):
        self.cam.start_recording()
    def stop_Recording(self):
        self.cam.stop_recording()