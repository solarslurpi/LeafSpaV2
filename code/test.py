from LeafSpa import LeafSpa
import time


l = LeafSpa()
l.start()
time.sleep(10)
print("hello about to stop")
l.stop()
