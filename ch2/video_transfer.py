import cv2 


videoCapture = cv2.VideoCapture("../source_video/vid_1.mp4")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter("../output_video/MyOutputVid.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()

videoCapture.release()
videoWriter.release()
cv2.destroyAllWindows()