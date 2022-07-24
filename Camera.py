import cv2


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def capture(self):
        self.cap = cv2.VideoCapture(0)
        # Capture frame
        for i in range(20):
            ret, frame = self.cap.read()

        if ret:
            cv2.imwrite('image.jpg', frame)
            im = cv2.imencode('.jpg', frame)[1].tobytes()
            self.cap.release()
            return im

