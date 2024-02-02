import cv2
import json
import sys
import os
import time


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)

sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..')))

import notecard  # noqa: E402

productUID = "xxxxxxxxxxxxxxxxx"

if sys.implementation.name != 'cpython':
 raise Exception("Please run this example in a CPython environment.")

from periphery import I2C  # noqa: E402

def NotecardExceptionInfo(exception):
 """Construct a formatted Exception string.

    Args:
        exception (Exception): An exception object.

    Returns:
        string: a summary of the exception with line number and details.
    """
    s1 = '{}'.format(sys.exc_info()[-1].tb_lineno)
    s2 = exception.__class__.__name__
 return "line " + s1 + ": " + s2 + ": " + ' '.join(map(str, exception.args))


def configure_notecard(card):
 
    req={"req":"card.wifi","ssid":"xxxxx","password":"xxxxx"}
    card.Transaction(req)
    time.sleep(5)


    req = {"req": "hub.set"}
    req["product"] = productUID
    req["mode"] = "continuous"

 try:
        card.Transaction(req)
 except Exception as exception:
        print("Transaction error: " + NotecardExceptionInfo(exception))
        time.sleep(5)


def get_temp_and_voltage(card):
    temp = 0
    voltage = 0

 try:
        req = {"req": "card.temp"}
        rsp = card.Transaction(req)
        temp = rsp["value"]

        req = {"req": "card.voltage"}
        rsp = card.Transaction(req)
        voltage = rsp["value"]
 except Exception as exception:
        print("Transaction error: " + NotecardExceptionInfo(exception))
        time.sleep(5)

 return temp, voltage


def main():
 """Connect to Notcard and run a transaction test."""
    print("Opening port...")
 try:
        port = I2C("/dev/i2c-1")
 except Exception as exception:
 raise Exception("error opening port: "
                        + NotecardExceptionInfo(exception))

    print("Opening Notecard...")
 try:
        card = notecard.OpenI2C(port, 0, 0, debug=True)
 except Exception as exception:
 raise Exception("error opening notecard: "
                        + NotecardExceptionInfo(exception))

 # If success, configure the Notecard and send some data
    configure_notecard(card)
 
 
 while(True):
      ret, frame = cap.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

 for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected")
 
        temp, voltage = get_temp_and_voltage(card)
 
        req = {"req": "note.add"}
        req["sync"] = True
        req["body"] = {"temp": temp, "voltage": voltage,"status":"fire_detected","Alarm":1}

 try:
          card.Transaction(req)
 except Exception as exception:
          print("Transaction error: " + NotecardExceptionInfo(exception))
          time.sleep(10)

      cv2.imshow('frame', frame)
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break
main()