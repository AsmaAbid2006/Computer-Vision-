from moviepy.editor import VideoFileClip,vfx
def load_clip(input_video):
    clip = VideoFileClip(input_video)
    return clip
def flip_clip(clip):
    flipped_clip = clip.fx(vfx.mirror_y)
    return flipped_clip
def save_clip(clip, output_video):
    clip.write_videofile(output_video, codec='libx264', fps=clip.fps)
    clip.close()
    if __name__ == "_main_":
     input_video = 'Task6/video1.mp4'
     output_video = 'Task4/FlippedVideo.mp4'
    clip = load_clip(input_video)
    flipped_clip = flip_clip(clip)
    save_clip(flipped_clip, output_video)