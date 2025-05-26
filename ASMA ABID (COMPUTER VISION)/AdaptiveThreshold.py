import skvideo.io
import cv2
def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return thresh
def main(input_video, output_video):
    videogen = skvideo.io.vreader(input_video)
    writer = skvideo.io.FFmpegWriter(output_video, inputdict={'-r': '30'}, outputdict={'-r': '30'})
    for frame in videogen:
        processed_frame = process_frame(frame)
        writer.writeFrame(processed_frame)
        cv2.imshow('Output', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    writer.close()
    cv2.destroyAllWindows()    
    print(f"Processed video saved as: {output_video}")
if __name__ == "__main__":
    input_video = 'Task6/video1.mp4'
    output_video = 'Task4/AdaptiveThreshold.mp4'
    main(input_video, output_video)
