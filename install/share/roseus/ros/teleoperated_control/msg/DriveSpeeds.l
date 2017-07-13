;; Auto-generated. Do not edit!


(when (boundp 'teleoperated_control::DriveSpeeds)
  (if (not (find-package "TELEOPERATED_CONTROL"))
    (make-package "TELEOPERATED_CONTROL"))
  (shadow 'DriveSpeeds (find-package "TELEOPERATED_CONTROL")))
(unless (find-package "TELEOPERATED_CONTROL::DRIVESPEEDS")
  (make-package "TELEOPERATED_CONTROL::DRIVESPEEDS"))

(in-package "ROS")
;;//! \htmlinclude DriveSpeeds.msg.html


(defclass teleoperated_control::DriveSpeeds
  :super ros::object
  :slots (_left_speed _right_speed ))

(defmethod teleoperated_control::DriveSpeeds
  (:init
   (&key
    ((:left_speed __left_speed) 0.0)
    ((:right_speed __right_speed) 0.0)
    )
   (send-super :init)
   (setq _left_speed (float __left_speed))
   (setq _right_speed (float __right_speed))
   self)
  (:left_speed
   (&optional __left_speed)
   (if __left_speed (setq _left_speed __left_speed)) _left_speed)
  (:right_speed
   (&optional __right_speed)
   (if __right_speed (setq _right_speed __right_speed)) _right_speed)
  (:serialization-length
   ()
   (+
    ;; float32 _left_speed
    4
    ;; float32 _right_speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _left_speed
       (sys::poke _left_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _right_speed
       (sys::poke _right_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _left_speed
     (setq _left_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _right_speed
     (setq _right_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get teleoperated_control::DriveSpeeds :md5sum-) "24112a9f04d430cb35b00cce81421a51")
(setf (get teleoperated_control::DriveSpeeds :datatype-) "teleoperated_control/DriveSpeeds")
(setf (get teleoperated_control::DriveSpeeds :definition-)
      "float32 left_speed
float32 right_speed
")



(provide :teleoperated_control/DriveSpeeds "24112a9f04d430cb35b00cce81421a51")


