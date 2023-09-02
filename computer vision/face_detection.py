import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time 

model_path='computer vision/models/blaze_face_short_range.tflite'
cam=cv2.VideoCapture(0)
results=[] 

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
FaceDetectorResult = mp.tasks.vision.FaceDetectorResult
VisionRunningMode = mp.tasks.vision.RunningMode


# Create a face detector instance with the live stream mode:
def show_result(result: FaceDetectorResult, output_image: mp.Image, timestamp_ms: int):
    print('face detector result: {}'.format(result))
    results.append(result)


options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=show_result)
with FaceDetector.create_from_options(options) as detector:
    while cam.isOpened():
        status,image=cam.read()
        mp_image=mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        timestamp= int(time.time() * 1000)
        print(timestamp)
        detector.detect_async(mp_image,timestamp)
        
        if results:
            detection_data=results.pop()
            for face in detection_data.detections:
                bb=face.bounding_box
                x=bb.origin_x
                y=bb.origin_y
                w=bb.width
                h=bb.height
                cv2.rectangle(
                    image,
                    (x,y),
                    (x+w,y+h),
                    (0,255,0),
                    1
                )
                cnf= round(face.categories[0].score,1)
                image=cv2.putText(
                    image,f"{cnf}%",(x,y-10),
                    cv2.FONT_HERSHEY_COMPLEX,.5,
                    (0,255,0),1,
                )
                
        cv2.imshow("output",image)
                # print(x,y,w,h)
                # print(face)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()