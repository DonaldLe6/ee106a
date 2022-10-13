import rospy
import tf2_ros
import sys


def controller(base, target):
  tfBuffer = tf2_ros.Buffer()
  tfListener = tf2_ros.TransformListener(tfBuffer)
  r = rospy.Rate(10)

  while not rospy.is_shutdown():
    try:
      trans = tfBuffer.lookup_transform(base, target, rospy.Time())
      print(trans)

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
      pass
    # Use our rate object to sleep until it is time to publish again
    r.sleep()

if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method

  #Run this program as a new node in the ROS computation graph 
  #called /turtlebot_controller.
  rospy.init_node('tf_listener', anonymous=True)

  try:
    controller(sys.argv[1], sys.argv[2])

  except rospy.ROSInterruptException:
    pass