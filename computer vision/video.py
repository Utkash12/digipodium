import cv2
VIDEO_PATH=r"C:\Users\Utkarsh\Downloads\pexels-matthias-groeneveld-17870383 (1080p).mp4"
vid=cv2.VideoCapture(VIDEO_PATH) # create a video capture object
while True:
    status,img =vid.read()
    if not status:
        print('video is not available')
        break
    # vision operations
    img=cv2.resize(img,None,fx=0.25,fy=0.25)
    cv2.imshow('video',img)
    key=cv2.waitKey(40)
    if key==27:
        break
cv2.destroyAllWindows()
vid.release() # release the video capture object