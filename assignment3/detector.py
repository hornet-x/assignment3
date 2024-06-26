import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image, CompressedImage

import cv2
from cv_bridge import CvBridge

class Detector(Node):

    def __init__(self):
        super().__init__("detector")
        self.pub_debug_img = self.create_publisher(Image, "/detected/debug_img", 10)
        self.sub_image_feed = self.create_subscription(
            CompressedImage,
            "/auv/bot_cam/image_color/compressed",
            self.image_feed_callback,
            10)
        self.bridge = CvBridge()

    def image_feed_callback(self, msg):
        # Feel free to modify this callback function, or add other functions in any way you deem fit

        # Here is sample code for converting a coloured image to gray scale using opencv
        cv_img = self.bridge.compressed_imgmsg_to_cv2(msg)
        transformed_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        img_msg = self.bridge.cv2_to_imgmsg(transformed_img, encoding="mono8")

        self.pub_debug_img.publish(img_msg)
    
def main(args=None):
    rclpy.init(args=args)
    detector = Detector()
    rclpy.spin(detector)

    # Below lines are not strictly necessary
    detector.destroy_node()
    rclpy.shutdown()
        
if __name__=='__main__':
    main()
