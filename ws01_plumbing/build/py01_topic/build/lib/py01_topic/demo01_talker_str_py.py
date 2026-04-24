"""  
    需求：以某个固定频率发送文本“hello world!”，文本后缀编号，每发送一条消息，编号递增1。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建发布方；
            3-2.创建定时器；
            3-3.组织消息并发布。
        4.调用spin函数，并传入节点对象；
        5.释放资源。
"""

# 1. 导入包
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# 3. 定义节点类
class Talker(Node):
    def __init__(self):
        super().__init__("talker_node_py")
        self.get_logger().info("发布方创建了(python)!")

        self.count = 0
        self.publisher = self.create_publisher(String, "chatter", 10)
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        message = String()
        message.data = "hello world(python)!" + str(self.count)
        self.publisher.publish(message)
        self.get_logger().info(f"发布的数据: {message.data}")
        self.count += 1

def main():
    rclpy.init()
    rclpy.spin(Talker())
    rclpy.shutdown()

if __name__ == '__main__':
    main()