#!/usr/bin/env python3
"""Week 4 turtlesim motion example: publish velocity commands."""

try:
    import rclpy
    from geometry_msgs.msg import Twist
except ImportError:
    rclpy = None
    Twist = None


def build_circle_command(linear=2.0, angular=1.0):
    if Twist is None:
        return {"linear_x": linear, "angular_z": angular}
    msg = Twist()
    msg.linear.x = linear
    msg.angular.z = angular
    return msg


def main():
    command = build_circle_command()
    print("Circle command:", command)
    print("Run inside ROS2 to publish this command to /turtle1/cmd_vel.")


if __name__ == "__main__":
    main()
