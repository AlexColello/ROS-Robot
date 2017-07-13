; Auto-generated. Do not edit!


(cl:in-package teleoperated_control-msg)


;//! \htmlinclude DriveSpeeds.msg.html

(cl:defclass <DriveSpeeds> (roslisp-msg-protocol:ros-message)
  ((left_speed
    :reader left_speed
    :initarg :left_speed
    :type cl:float
    :initform 0.0)
   (right_speed
    :reader right_speed
    :initarg :right_speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass DriveSpeeds (<DriveSpeeds>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveSpeeds>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveSpeeds)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name teleoperated_control-msg:<DriveSpeeds> is deprecated: use teleoperated_control-msg:DriveSpeeds instead.")))

(cl:ensure-generic-function 'left_speed-val :lambda-list '(m))
(cl:defmethod left_speed-val ((m <DriveSpeeds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader teleoperated_control-msg:left_speed-val is deprecated.  Use teleoperated_control-msg:left_speed instead.")
  (left_speed m))

(cl:ensure-generic-function 'right_speed-val :lambda-list '(m))
(cl:defmethod right_speed-val ((m <DriveSpeeds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader teleoperated_control-msg:right_speed-val is deprecated.  Use teleoperated_control-msg:right_speed instead.")
  (right_speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveSpeeds>) ostream)
  "Serializes a message object of type '<DriveSpeeds>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'left_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'right_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveSpeeds>) istream)
  "Deserializes a message object of type '<DriveSpeeds>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveSpeeds>)))
  "Returns string type for a message object of type '<DriveSpeeds>"
  "teleoperated_control/DriveSpeeds")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveSpeeds)))
  "Returns string type for a message object of type 'DriveSpeeds"
  "teleoperated_control/DriveSpeeds")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveSpeeds>)))
  "Returns md5sum for a message object of type '<DriveSpeeds>"
  "24112a9f04d430cb35b00cce81421a51")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveSpeeds)))
  "Returns md5sum for a message object of type 'DriveSpeeds"
  "24112a9f04d430cb35b00cce81421a51")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveSpeeds>)))
  "Returns full string definition for message of type '<DriveSpeeds>"
  (cl:format cl:nil "float32 left_speed~%float32 right_speed~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveSpeeds)))
  "Returns full string definition for message of type 'DriveSpeeds"
  (cl:format cl:nil "float32 left_speed~%float32 right_speed~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveSpeeds>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveSpeeds>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveSpeeds
    (cl:cons ':left_speed (left_speed msg))
    (cl:cons ':right_speed (right_speed msg))
))
