#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Display:
    def __init__(self):
        self.bridge = CvBridge()
        self.set_detector_param()
        self.raw_image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.filter_img)


    def set_detector_param(self):
        self.params = cv2.SimpleBlobDetector_Params()

        # Change thresholds
        self.params.minThreshold = 50;
        self.params.maxThreshold = 100;

        # Filter by Area.
        self.params.filterByArea = True
        self.params.minArea = 30
        self.params.minArea = 20000

        # Filter by Circularity
        self.params.filterByCircularity = True
        self.params.minCircularity = 0.1

        # Filter by Convexity
        self.params.filterByConvexity = True
        self.params.minConvexity = 0.5

        # Filter by Inertia
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.5

        self.detector = cv2.SimpleBlobDetector_create(self.params)

    def filter_img(self, msg):
        try:
            self.current_img = self.bridge.imgmsg_to_cv2(msg, "mono8")
            self.color_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            #self.hsv_img = cv2.cvtColor(self.color_img, cv2.COLOR_BGR2HSV)
            #mask = cv2.inRange()
            
            threshold = 140
            assignvalue = 255
            ret, thresh = cv2.threshold(self.current_img,
                          threshold,
                          assignvalue,
                          cv2.THRESH_BINARY)

            #reverse_mask = 255 - thresh
            if self.detector:
                ##NOT WORKING MAYBE TRYING DIFFERENT MASKING
                keypoints = self.detector.detect(thresh)
                print(keypoints)

            cv2.waitKey(3)
            cv2.imshow("masked image", thresh)

            #cv2.rectangle(self.color_img,(384,0),(510,128),(0,255,0),3)
            #cv2.imshow("color image", self.color_img)

        except CvBridgeError as e:
            print(e)

if __name__ == '__main__':
    rospy.init_node('display_node')
    Display()
    rospy.spin()
