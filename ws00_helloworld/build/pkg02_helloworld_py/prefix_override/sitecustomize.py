import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zhiyan/ros2_tutorial/ws00_helloworld/install/pkg02_helloworld_py'
