import cv2

face_cascade = cv2.CascadeClassifier("/Users/aahan/Downloads/facedetection-master/haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

while True:
    _, cap = vid.read()
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(cap, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("Face Recognition", cap)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exited")
        break
vid.release()

if cv2.rectangle:
    print("Faces Detected during this session")