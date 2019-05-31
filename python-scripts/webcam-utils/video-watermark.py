import numpy as np
import os
import cv2

#WEBCAM MAX RES 640 x 480
from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermark.mp4'
frames_per_second = 24
config = CFEVideoConf(cap, filepath=save_path, res='480')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_second, config.dims)

img_path = 'logo.jpg'
logo = cv2.imread(img_path, -1)

watermark = image_resize(logo, height=50)
cv2.imshow('watermark', watermark)

while (True):
	# capture frame by frame
    ret, frame = cap.read()
    # out.write(frame)
    # display the frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()