/*
 需求：在终端输出文本hello world。
 流程：
     1.包含头文件；
     2.初始化Ros2客户端
     3.创建节点指针；
     4.输出日志；
     5.释放资源。

*/

#include "rclcpp/rclcpp.hpp"

int main(int argc, char ** argv){
  
  // 2.初始化 ROS2
  rclcpp::init(argc,argv);
  // 3.创建节点
  auto node = rclcpp::Node::make_shared("helloworld_node_cpp");
  // 4.输出文本
  RCLCPP_INFO(node->get_logger(),"hello world!");
  // 5.释放资源
  rclcpp::shutdown();
  return 0;
}
