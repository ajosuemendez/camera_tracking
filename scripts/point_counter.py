#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2

class PointsCounter:
    def __init__(self):
        self.cp2_subscriber = rospy.Subscriber("/camera/depth/points", PointCloud2, self.calc_total_cl_points)

    def calc_total_cl_points(self, msg):
        cloud_points = list(point_cloud2.read_points(msg, skip_nans=True, field_names = ("x", "y", "z")))
        num_points = np.shape(cloud_points)[0]
        print("Number of Points:", num_points)
if __name__ == '__main__':
    rospy.init_node('points_counter')
    PointsCounter()
    rospy.spin()
