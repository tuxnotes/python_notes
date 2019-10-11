import os, cv2, time, struct, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

class JpegStream(Thread):
    def __init__(self, camera):
        super().__init__()
        self.cap =cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        pw = self.pipes.pop(pr)
        sefl.lock.release()
        so.close(pr)
        so.close(pw)

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY,40))
                yield data.tostring

    def send_frame(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.values(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
            self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send_frame(frame)


class JpegRetriever:


