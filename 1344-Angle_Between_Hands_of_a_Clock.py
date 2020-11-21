class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """

        """
        - clarification questions: range of hour and minute - 1 <= hour <= 12, 0 <= minutes <= 59
        """
        ANGLE_PER_HOUR = 30
        ANGLE_HOUR_PER_MINUTE = 0.5
        ANGLE_PER_MINUTE = 6
        
        angle_hour = hour % 12 * ANGLE_PER_HOUR + minutes * ANGLE_HOUR_PER_MINUTE
        angle_minute = minutes * ANGLE_PER_MINUTE
        
        # return angle_minute
        res = abs(angle_minute - angle_hour)
        return res if res <= 180 else 360 - res

        """
        - Leetcode solution
        """
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)