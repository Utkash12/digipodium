import cv2
CAM_IDX=0
cam=cv2.VideoCapture(CAM_IDX) # 0: default camera create a video capture object
cam.read() # read a frame from the video capture object
while cam.isOpened():   
    status, img=cam.read()
    if status:
        cv2.imshow('webcam', img) # display the image
        key=cv2.waitKey(10)
        if key==27:
            break 
    else:
        print('webcam is not available')
        break
cv2.destroyAllWindows()
cam.release() # release the video capture object