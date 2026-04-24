import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zhiyan/ros2_tutorial/ws01_plumbing/install/py01_topic'
