from moviepy.editor import VideoFileClip
def load_clip(input_video):
    clip = VideoFileClip(input_video)
    return clip
def crop_clip(clip, x1, y1, x2, y2):
    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
    return cropped_clip
def save_clip(clip, output_video):
    clip.write_videofile(output_video, codec='libx264', fps=clip.fps)
    clip.close()
if __name__ == "_main_":
    input_video = 'Task6/video1.mp4'
    output_video = 'Task4/CroppedVideo.mp4'
    x1, y1 = 100, 100 
    x2, y2 = 500, 400  
    clip = load_clip(input_video)

    # Crop the video clip
    cropped_clip = crop_clip(clip, x1, y1, x2, y2)

    # Save the cropped clip
    save_clip(cropped_clip, output_video)