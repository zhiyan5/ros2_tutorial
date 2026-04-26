// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from base_interfaces_demo:msg/Student.idl
// generated code does not contain a copyright notice

#ifndef BASE_INTERFACES_DEMO__MSG__DETAIL__STUDENT__BUILDER_HPP_
#define BASE_INTERFACES_DEMO__MSG__DETAIL__STUDENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "base_interfaces_demo/msg/detail/student__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace base_interfaces_demo
{

namespace msg
{


}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::base_interfaces_demo::msg::Student>()
{
  return ::base_interfaces_demo::msg::Student(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace base_interfaces_demo

#endif  // BASE_INTERFACES_DEMO__MSG__DETAIL__STUDENT__BUILDER_HPP_
