import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture("edit.mp4")
c = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_color = frame[y:y + h, x:x + w]
        # cv2.imwrite("temp_data/" + str(c) + '_+faces.jpg', roi_color)
        c += 1
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

#300