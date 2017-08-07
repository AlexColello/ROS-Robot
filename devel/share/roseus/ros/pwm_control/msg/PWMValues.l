;; Auto-generated. Do not edit!


(when (boundp 'pwm_control::PWMValues)
  (if (not (find-package "PWM_CONTROL"))
    (make-package "PWM_CONTROL"))
  (shadow 'PWMValues (find-package "PWM_CONTROL")))
(unless (find-package "PWM_CONTROL::PWMVALUES")
  (make-package "PWM_CONTROL::PWMVALUES"))

(in-package "ROS")
;;//! \htmlinclude PWMValues.msg.html


(defclass pwm_control::PWMValues
  :super ros::object
  :slots (_outputs ))

(defmethod pwm_control::PWMValues
  (:init
   (&key
    ((:outputs __outputs) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _outputs __outputs)
   self)
  (:outputs
   (&optional __outputs)
   (if __outputs (setq _outputs __outputs)) _outputs)
  (:serialization-length
   ()
   (+
    ;; float32[] _outputs
    (* 4    (length _outputs)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _outputs
     (write-long (length _outputs) s)
     (dotimes (i (length _outputs))
       (sys::poke (elt _outputs i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _outputs
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _outputs (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _outputs i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get pwm_control::PWMValues :md5sum-) "2710679c2f2cf91e01db75d8355eaf6d")
(setf (get pwm_control::PWMValues :datatype-) "pwm_control/PWMValues")
(setf (get pwm_control::PWMValues :definition-)
      "float32[] outputs
")



(provide :pwm_control/PWMValues "2710679c2f2cf91e01db75d8355eaf6d")


