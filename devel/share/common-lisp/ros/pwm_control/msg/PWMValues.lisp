; Auto-generated. Do not edit!


(cl:in-package pwm_control-msg)


;//! \htmlinclude PWMValues.msg.html

(cl:defclass <PWMValues> (roslisp-msg-protocol:ros-message)
  ((outputs
    :reader outputs
    :initarg :outputs
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass PWMValues (<PWMValues>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PWMValues>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PWMValues)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pwm_control-msg:<PWMValues> is deprecated: use pwm_control-msg:PWMValues instead.")))

(cl:ensure-generic-function 'outputs-val :lambda-list '(m))
(cl:defmethod outputs-val ((m <PWMValues>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pwm_control-msg:outputs-val is deprecated.  Use pwm_control-msg:outputs instead.")
  (outputs m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PWMValues>) ostream)
  "Serializes a message object of type '<PWMValues>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'outputs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'outputs))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PWMValues>) istream)
  "Deserializes a message object of type '<PWMValues>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'outputs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'outputs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PWMValues>)))
  "Returns string type for a message object of type '<PWMValues>"
  "pwm_control/PWMValues")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PWMValues)))
  "Returns string type for a message object of type 'PWMValues"
  "pwm_control/PWMValues")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PWMValues>)))
  "Returns md5sum for a message object of type '<PWMValues>"
  "2710679c2f2cf91e01db75d8355eaf6d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PWMValues)))
  "Returns md5sum for a message object of type 'PWMValues"
  "2710679c2f2cf91e01db75d8355eaf6d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PWMValues>)))
  "Returns full string definition for message of type '<PWMValues>"
  (cl:format cl:nil "float32[] outputs~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PWMValues)))
  "Returns full string definition for message of type 'PWMValues"
  (cl:format cl:nil "float32[] outputs~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PWMValues>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'outputs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PWMValues>))
  "Converts a ROS message object to a list"
  (cl:list 'PWMValues
    (cl:cons ':outputs (outputs msg))
))
