// Generated by gencpp from file hrwros_gazebo/VacuumGripperControlResponse.msg
// DO NOT EDIT!


#ifndef HRWROS_GAZEBO_MESSAGE_VACUUMGRIPPERCONTROLRESPONSE_H
#define HRWROS_GAZEBO_MESSAGE_VACUUMGRIPPERCONTROLRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace hrwros_gazebo
{
template <class ContainerAllocator>
struct VacuumGripperControlResponse_
{
  typedef VacuumGripperControlResponse_<ContainerAllocator> Type;

  VacuumGripperControlResponse_()
    : success(false)  {
    }
  VacuumGripperControlResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> const> ConstPtr;

}; // struct VacuumGripperControlResponse_

typedef ::hrwros_gazebo::VacuumGripperControlResponse_<std::allocator<void> > VacuumGripperControlResponse;

typedef boost::shared_ptr< ::hrwros_gazebo::VacuumGripperControlResponse > VacuumGripperControlResponsePtr;
typedef boost::shared_ptr< ::hrwros_gazebo::VacuumGripperControlResponse const> VacuumGripperControlResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator1> & lhs, const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator1> & lhs, const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hrwros_gazebo

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hrwros_gazebo/VacuumGripperControlResponse";
  }

  static const char* value(const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VacuumGripperControlResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hrwros_gazebo::VacuumGripperControlResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HRWROS_GAZEBO_MESSAGE_VACUUMGRIPPERCONTROLRESPONSE_H
