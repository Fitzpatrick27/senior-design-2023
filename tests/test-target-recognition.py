import depthai as dai
import numpy as np
import time
from pipeline import *


# Connect to device and start pipeline
with dai.Device(create_pipeline(), usb2Mode=True) as device:
    preview = device.getOutputQueue("preview", 4, False)
    tracklets = device.getOutputQueue("tracklets", 4, False)

    startTime = time.monotonic()
    counter = 0
    fps = 0
    color = (255, 255, 255)

    # open a csv file
    file  = open("data.csv", "w")
    file.write("x,y,z\n")

    while(True):
        imgFrame = preview.get()
        track = tracklets.get()

        counter+=1
        current_time = time.monotonic()
        if (current_time - startTime) > 1 :
            fps = counter / (current_time - startTime)
            counter = 0
            startTime = current_time

        frame = imgFrame.getCvFrame()
        trackletsData = track.tracklets
        for t in trackletsData:
            if (t.status.name == "LOST"):
                continue
            roi = t.roi.denormalize(frame.shape[1], frame.shape[0])
            x1 = int(roi.topLeft().x)
            y1 = int(roi.topLeft().y)
            x2 = int(roi.bottomRight().x)
            y2 = int(roi.bottomRight().y)
            label = t.label

            print ("x: " , t.spatialCoordinates.x, "y: ", t.spatialCoordinates.y, "z: ", (t.spatialCoordinates.z),"\n")

            file.write("%.2f,%.2f,%.2f\n" % (t.spatialCoordinates.x, t.spatialCoordinates.y, t.spatialCoordinates.z))
