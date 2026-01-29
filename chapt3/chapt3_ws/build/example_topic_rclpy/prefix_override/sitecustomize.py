import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/andinm/d2lros2/chapt3/chapt3_ws/install/example_topic_rclpy'
