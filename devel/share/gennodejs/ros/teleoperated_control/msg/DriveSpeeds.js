// Auto-generated. Do not edit!

// (in-package teleoperated_control.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class DriveSpeeds {
  constructor() {
    this.left_speed = 0.0;
    this.right_speed = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type DriveSpeeds
    // Serialize message field [left_speed]
    bufferInfo = _serializer.float32(obj.left_speed, bufferInfo);
    // Serialize message field [right_speed]
    bufferInfo = _serializer.float32(obj.right_speed, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type DriveSpeeds
    let tmp;
    let len;
    let data = new DriveSpeeds();
    // Deserialize message field [left_speed]
    tmp = _deserializer.float32(buffer);
    data.left_speed = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [right_speed]
    tmp = _deserializer.float32(buffer);
    data.right_speed = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'teleoperated_control/DriveSpeeds';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '24112a9f04d430cb35b00cce81421a51';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 left_speed
    float32 right_speed
    `;
  }

};

module.exports = DriveSpeeds;
