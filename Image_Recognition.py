import cv2
f = 0
face_cascade = cv2.CascadeClassifier("/Users/aahan/Downloads/facedetection-master/haarcascade_frontalface_default.xml")

img = cv2.imread("/Users/aahan/Desktop/samefacemany.jpgq")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    if cv2.rectangle:
        f += 1
        print("%s faces detected" % (f))

if __name__ == "__main__":
    cv2.imshow("Face Detected", img)
    cv2.waitKey()

    if cv2.waitKey:
        print("Exited")