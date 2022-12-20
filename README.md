# camera_tracking

run the command: **roslaunch camera_tracking sim.launch** to start the simulation. This will launch Gazebo, Rviz and a basic node that counts the amount of points given by the camera from a PointCloud2 message.

In gazebo you can add a kinect_camera and more items in the environement to test it.

In a new Terminal you can call the following service to get the total amount of points: **rosservice call /get_total_points "data: true"**

You can also get all the x, y, z coordinates for each point by running: **rosservice call /get_current_points "data: true"**
