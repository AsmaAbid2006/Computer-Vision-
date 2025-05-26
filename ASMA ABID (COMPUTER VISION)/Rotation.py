from moviepy.editor import VideoFileClip
def load_clip(input_video):
    clip = VideoFileClip(input_video)
    return clip
def rotate_clip(clip, angle):
    rotated_clip = clip.rotate(angle)
    return rotated_clip
def save_clip(clip, output_video):
    clip.write_videofile(output_video, codec='libx264', fps=clip.fps)
    clip.close()
if __name__ == "_main_":
    input_video = 'Task6/video1.mp4'
    output_video = 'Task4/RotatedVideo.mp4'
    rotation_angle = 90 
    clip = load_clip(input_video)
    rotated_clip = rotate_clip(clip, rotation_angle)
    save_clip(rotated_clip, output_video)