"""  
    需求：创建客户端，解析客户端提交的数据并响应结果
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建客户端；
            3-2.创建定时器；
            3-3.组织消息并发布。
        4.调用spin函数，并传入节点对象；
        5.释放资源。
"""

# 1. 导入包
import rclpy
from rclpy.node import Node

# 3. 定义节点类
class AddlntsServer(Node):
    def __init__(self):
        super().__init__("add_lnts_server_node_py")
        self.get_logger().info("服务端创建了!(python)")

def main():
    rclpy.init()
    rclpy.spin(AddlntsServer())
    rclpy.shutdown()

if __name__ == '__main__':
    main()