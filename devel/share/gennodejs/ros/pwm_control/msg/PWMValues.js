// Auto-generated. Do not edit!

// (in-package pwm_control.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class PWMValues {
  constructor() {
    this.outputs = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type PWMValues
    // Serialize the length for message field [outputs]
    bufferInfo = _serializer.uint32(obj.outputs.length, bufferInfo);
    // Serialize message field [outputs]
    obj.outputs.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type PWMValues
    let tmp;
    let len;
    let data = new PWMValues();
    // Deserialize array length for message field [outputs]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [outputs]
    data.outputs = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.outputs[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'pwm_control/PWMValues';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2710679c2f2cf91e01db75d8355eaf6d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] outputs
    `;
  }

};

module.exports = PWMValues;
