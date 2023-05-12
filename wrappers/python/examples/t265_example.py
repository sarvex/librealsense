#!/usr/bin/python
# -*- coding: utf-8 -*-
## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2019 Intel Corporation. All Rights Reserved.

#####################################################
##           librealsense T265 example             ##
#####################################################

# First import the library
import pyrealsense2 as rs

# Declare RealSense pipeline, encapsulating the actual device and sensors
pipe = rs.pipeline()

# Build config object and request pose data
cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

# Start streaming with requested config
pipe.start(cfg)

try:
    for _ in range(50):
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()

        if pose := frames.get_pose_frame():
            # Print some of the pose data to the terminal
            data = pose.get_pose_data()
            print(f"Frame #{pose.frame_number}")
            print(f"Position: {data.translation}")
            print(f"Velocity: {data.velocity}")
            print(f"Acceleration: {data.acceleration}\n")

finally:
    pipe.stop()
