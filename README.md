# Hornet X Software Assignment 3

This repository contains a ROS2 package called "assignment3". It includes a basic detector node.
Your task is to implement a node that draws a bounding box around the red regions of the roulette wheel and label it "red".
Refer to the third workshop for more details.

Zip and email your solution to hornetxauv2425@gmail.com with subject [Software Homework 3] \<Name\>.

## Playing ROS2 bags

For this assignment you will have to make use of a ROS2 bag recording from a previou year.
The ROS2 bag files can be downloaded [here](https://drive.google.com/file/d/1L2Q0CZNCxA--sK7Znj0MpWLe7PkKXeO2/view?usp=drive_link)

Simply untar and play the bag file

```bash
tar -xvf session3bags.tar
ros2 bag play session3bags
```

This should start publishing ROS2 CompressedImage messages to the `/auv/bot_cam/image_color/compressed` topic,
which you can verify by running thr `ros2 topic list` command.

## Setting up the assignment

If you have followed the set up instructions from the workshop,
you should have all the dependencies (mainly OpenCV) installed and ready to go.

To run the default code, first ensure that you have `session3bags` playing.
Then, in a seperate terminal add this package to your workspace and build

```bash
colcon build --packages-select assignment3
source install/setup.bash
ros2 run assignment3 detector
```

The default code publishes a gray scaled version of the images from the `session3bags` to the `/detected/debug_img` topic.

If you are using RQT to visualise your images,
you should be able to display the gray scaled version of the images like so

![image](https://github.com/hornetnine/assignment3/assets/143057023/1d3555c7-bae0-49b2-addb-bc664ef30c7a)

Note the original image from the bag file is on the left, and the published image is on the right.
