import skvideo.io
import numpy as np
from scipy.ndimage import gaussian_filter
def load_video(input_video):
    videogen = skvideo.io.vreader(input_video)
    frames = list(videogen)
    return frames
def smooth_frame(frame):
    smoothed_frame = gaussian_filter(frame, sigma=1.0)
    return smoothed_frame
def smooth_video(frames):
    smoothed_frames = [smooth_frame(frame) for frame in frames]
    return smoothed_frames
def save_video(frames, output_video):
    skvideo.io.vwrite(output_video, frames)
if __name__ == "_main_":
    input_video = 'Task6/video1.mp4'
    output_video = 'Task4/smoothed_video.mp4'
    frames = load_video(input_video)
    smoothed_frames = smooth_video(frames)
    save_video(smoothed_frames, output_video)