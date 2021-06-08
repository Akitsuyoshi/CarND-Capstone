from lowpass import LowPassFilter
from yaw_controller import YawController
from pid import PID
import rospy

GAS_DENSITY = 2.858
ONE_MPH = 0.44704


class Controller(object):
    def __init__(self, *args, **kwargs):
        # TODO: Implement
        self.yaw_controller = YawController()
        self.throttle_controller = PID()
        self.vel_lpf = LowPassFilter()

    def control(self, dbw_enabled, current_vel, linear_vel, angular_vel):
        # Return throttle, brake, steer
        if not dbw_enabled:
            self.throttle_controller.reset()
            return 0., 0., 0.

        return 1., 0., 0.
