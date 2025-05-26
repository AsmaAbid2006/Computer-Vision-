import skvideo.io
import numpy as np
def load_video(input_video):
    videogen = skvideo.io.vreader(input_video)
    frames = list(videogen)
    return frames
def bitwise_and_video(frames):
    result_frames = []
    for frame in frames:
        gray_frame = np.mean(frame, axis=2, dtype=np.uint8)  
        threshold = 100  
        masked_frame = np.where(gray_frame > threshold, 255, 0).astype(np.uint8)
        result_frames.append(np.stack([masked_frame, masked_frame, masked_frame], axis=2))
    return result_frames
def save_video(frames, output_video):
    skvideo.io.vwrite(output_video, frames)
    if __name__ == "_main_":
     input_video = 'Task6/video1.mp4'
     output_video = 'Task4/BitwiseOperations.mp4'
     
    frames = load_video(input_video)
    result_frames = bitwise_and_video(frames)
    save_video(result_frames, output_video)