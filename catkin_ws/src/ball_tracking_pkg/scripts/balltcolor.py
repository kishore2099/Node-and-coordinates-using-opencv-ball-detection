#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Point
cap = cv2.VideoCapture(0)
if not cap.isOpened():
 print("Cannot open camera")
 exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# class BallTrackerNode:
#     def __init__(self):
#         rospy.init_node("ball_tracker_node")
#         self.bridge = CvBridge()
#         self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.image_callback)
#         self.ball_pub = rospy.Publisher("/ball_coordinates", Point, queue_size=10)

#         # Create a window for displaying the camera feed
#         self.window_name = "Ball Tracking"
#         cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

#     def image_callback(self, image_msg):
#         try:
#             cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
#         except CvBridgeError as e:
#             rospy.logerr(e)
#             return

#         # Define the HSV range for the color of the ball (adjust as needed)
#         lower_hsv = np.array([30, 150, 50])
#         upper_hsv = np.array([45, 255, 255])

#         # Convert the image to HSV color space
#         hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

#         # Threshold the image to isolate the ball color
#         mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)

#         # Find contours in the masked image
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         if len(contours) > 0:
#             # Find the largest contour (the presumed ball)
#             max_contour = max(contours, key=cv2.contourArea)

#             # Get the center and radius of the ball
#             ((x, y), radius) = cv2.minEnclosingCircle(max_contour)
#             center = (int(x), int(y))

#             # Publish the coordinates of the ball to ROS
#             ball_coordinates = Point()
#             ball_coordinates.x = center[0]
#             ball_coordinates.y = center[1]
#             self.ball_pub.publish(ball_coordinates)

#             # Draw a circle around the detected ball
#             cv2.circle(cv_image, center, int(radius), (0, 255, 0), 2)  # Green circle with 2-pixel thickness

#             # Display the coordinates of the ball on the image
#             text = f"X: {center[0]}, Y: {center[1]}"
#             cv2.putText(cv_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Red text

#         # Display the camera feed
#         cv2.imshow(self.window_name, cv_image)
#         cv2.waitKey(1)  # Update the display (1 millisecond delay)

#     def run(self):
#         rospy.spin()
#         cv2.destroyAllWindows()  # Close OpenCV windows when the node is shut down

# if __name__ == "__main__":
#     try:
#         ball_tracker = BallTrackerNode()
#         ball_tracker.run()
#     except rospy.ROSInterruptException:
#         pass
