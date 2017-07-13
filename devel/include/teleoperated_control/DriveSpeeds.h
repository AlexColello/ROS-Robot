// Generated by gencpp from file teleoperated_control/DriveSpeeds.msg
// DO NOT EDIT!


#ifndef TELEOPERATED_CONTROL_MESSAGE_DRIVESPEEDS_H
#define TELEOPERATED_CONTROL_MESSAGE_DRIVESPEEDS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace teleoperated_control
{
template <class ContainerAllocator>
struct DriveSpeeds_
{
  typedef DriveSpeeds_<ContainerAllocator> Type;

  DriveSpeeds_()
    : left_speed(0.0)
    , right_speed(0.0)  {
    }
  DriveSpeeds_(const ContainerAllocator& _alloc)
    : left_speed(0.0)
    , right_speed(0.0)  {
  (void)_alloc;
    }



   typedef float _left_speed_type;
  _left_speed_type left_speed;

   typedef float _right_speed_type;
  _right_speed_type right_speed;




  typedef boost::shared_ptr< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> const> ConstPtr;

}; // struct DriveSpeeds_

typedef ::teleoperated_control::DriveSpeeds_<std::allocator<void> > DriveSpeeds;

typedef boost::shared_ptr< ::teleoperated_control::DriveSpeeds > DriveSpeedsPtr;
typedef boost::shared_ptr< ::teleoperated_control::DriveSpeeds const> DriveSpeedsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::teleoperated_control::DriveSpeeds_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace teleoperated_control

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'teleoperated_control': ['/home/erle/ROS-Robot/src/teleoperated_control/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "24112a9f04d430cb35b00cce81421a51";
  }

  static const char* value(const ::teleoperated_control::DriveSpeeds_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x24112a9f04d430cbULL;
  static const uint64_t static_value2 = 0x35b00cce81421a51ULL;
};

template<class ContainerAllocator>
struct DataType< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "teleoperated_control/DriveSpeeds";
  }

  static const char* value(const ::teleoperated_control::DriveSpeeds_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 left_speed\n\
float32 right_speed\n\
";
  }

  static const char* value(const ::teleoperated_control::DriveSpeeds_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.left_speed);
      stream.next(m.right_speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct DriveSpeeds_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::teleoperated_control::DriveSpeeds_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::teleoperated_control::DriveSpeeds_<ContainerAllocator>& v)
  {
    s << indent << "left_speed: ";
    Printer<float>::stream(s, indent + "  ", v.left_speed);
    s << indent << "right_speed: ";
    Printer<float>::stream(s, indent + "  ", v.right_speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TELEOPERATED_CONTROL_MESSAGE_DRIVESPEEDS_H