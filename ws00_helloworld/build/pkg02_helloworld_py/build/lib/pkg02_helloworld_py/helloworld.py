"""
需求：在终端输出文本hello world。
 流程：
     1.导包；
     2.初始化Ros2客户端
     3.创建节点；
     4.输出日志；
     5.释放资源。
"""
#1.导包
import rclpy
from rclpy.node import Node
#方式二
#自定义类
class MyNode(Node):
    def __init__(self):
        super().__init__("hello_node_py")
        self.get_logger().info("hello world!(python 继承方式)")

def main():
    #初始化
    rclpy.init()
    #创建对象
    node = MyNode()
    # ....
    #资源释放
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()