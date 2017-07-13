
(cl:in-package :asdf)

(defsystem "teleoperated_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DriveSpeeds" :depends-on ("_package_DriveSpeeds"))
    (:file "_package_DriveSpeeds" :depends-on ("_package"))
  ))