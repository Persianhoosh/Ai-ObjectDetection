
#Fallow me on:
#https://T.me/AiHoma
#https://medium.com/@AiHoma
#https://github.com/PersianHoosh

#pip install opencv-python rembg onnxruntime


import cv2
from rembg import remove

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("can not open camera")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("can not get frame")
            break
        
        cv2.imshow("Press Space to Capture", frame)
        key = cv2.waitKey(1)
        
        if key == 32:  # press Space
            cv2.imwrite("input.jpg", frame)
            print("image saved")
            break
    
    cap.release()
    cv2.destroyAllWindows()

def extract_person(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("can not find image")
        return
    
    with open(image_path, "rb") as f:
        image_no_bg = remove(f.read())
    
    output_filename = "out.png"
    with open(output_filename, "wb") as f:
        f.write(image_no_bg)
    
    print(f"extracted object saved: {output_filename}")

capture_image()
extract_person("input.jpg")
