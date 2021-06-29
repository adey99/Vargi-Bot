// Generated by gencpp from file pkg_ros_iot_bridge/msgRosIotFeedback.msg
// DO NOT EDIT!


#ifndef PKG_ROS_IOT_BRIDGE_MESSAGE_MSGROSIOTFEEDBACK_H
#define PKG_ROS_IOT_BRIDGE_MESSAGE_MSGROSIOTFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pkg_ros_iot_bridge
{
template <class ContainerAllocator>
struct msgRosIotFeedback_
{
  typedef msgRosIotFeedback_<ContainerAllocator> Type;

  msgRosIotFeedback_()
    : percentage_complete(0)  {
    }
  msgRosIotFeedback_(const ContainerAllocator& _alloc)
    : percentage_complete(0)  {
  (void)_alloc;
    }



   typedef int8_t _percentage_complete_type;
  _percentage_complete_type percentage_complete;





  typedef boost::shared_ptr< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct msgRosIotFeedback_

typedef ::pkg_ros_iot_bridge::msgRosIotFeedback_<std::allocator<void> > msgRosIotFeedback;

typedef boost::shared_ptr< ::pkg_ros_iot_bridge::msgRosIotFeedback > msgRosIotFeedbackPtr;
typedef boost::shared_ptr< ::pkg_ros_iot_bridge::msgRosIotFeedback const> msgRosIotFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator1> & lhs, const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.percentage_complete == rhs.percentage_complete;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator1> & lhs, const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pkg_ros_iot_bridge

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d5151973e38c593f60bed311537d61df";
  }

  static const char* value(const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd5151973e38c593fULL;
  static const uint64_t static_value2 = 0x60bed311537d61dfULL;
};

template<class ContainerAllocator>
struct DataType< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pkg_ros_iot_bridge/msgRosIotFeedback";
  }

  static const char* value(const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# feedback\n"
"int8 percentage_complete\n"
"\n"
;
  }

  static const char* value(const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.percentage_complete);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct msgRosIotFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pkg_ros_iot_bridge::msgRosIotFeedback_<ContainerAllocator>& v)
  {
    s << indent << "percentage_complete: ";
    Printer<int8_t>::stream(s, indent + "  ", v.percentage_complete);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PKG_ROS_IOT_BRIDGE_MESSAGE_MSGROSIOTFEEDBACK_H
