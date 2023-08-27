import cv2
CAM_IDX=0
cam=cv2.VideoCapture(CAM_IDX) # 0: default camera create a video capture object
cv2.namedWindow('canny')
lowthreshold=cv2.createTrackbar('Low Threshold',"canny",0,1000,lambda x:None)
highthreshold=cv2.createTrackbar('High Threshold',"canny",0,1000,lambda x:None)    
while cam.isOpened():
    state,img=cam.read()
    if not state:
        print('Camera is not available')
        break
    # basic filter
    im_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #2d
    im_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #3d
    # adv filter
    lt=cv2.getTrackbarPos('Low Threshold',"canny")
    ht=cv2.getTrackbarPos('High Threshold',"canny")
    im_canny=cv2.Canny(img,100,150)
    im_sobel=cv2.Sobel(im_gray,cv2.CV_64F,1,1,ksize=3)

    cv2.imshow('original',img)
    cv2.imshow('gray',im_gray)
    cv2.imshow('rgb',im_rgb)
    cv2.imshow('canny',im_canny)
    cv2.imshow('sobel',im_sobel)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break
cv2.destroyAllWindows()
cam.release() # release the video capture object