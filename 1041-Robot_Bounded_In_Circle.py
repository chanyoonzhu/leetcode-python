class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        """
        - if is bounded, if not return to original in one try, will return to the original in at most 4 attempts.
        - O(n), O(1)
        """
        TOTAL_DIRECTIONS = 4
        direction_steps = [0] * TOTAL_DIRECTIONS
        direction = 0 # direction, l + 1, r - 1
        for inst in instructions * TOTAL_DIRECTIONS:
            if inst == 'G':
                direction_steps[direction] += 1
            elif inst == 'L':
                direction = (direction + 1) % TOTAL_DIRECTIONS
            elif inst == 'R':
                direction = (direction - 1) % TOTAL_DIRECTIONS
        return (direction_steps[0] == direction_steps[2] and direction_steps[1] == direction_steps[3])

        """
        - Optimization: if ending direction is not same as starting direction, will return the original positin in at most 4 attempts
        - O(n), O(1)
        """
        TOTAL_DIRECTIONS = 4
        direction_steps = [0] * TOTAL_DIRECTIONS
        direction = 0 # direction, l + 1, r - 1
        for inst in instructions:
            if inst == 'G':
                direction_steps[direction] += 1
            elif inst == 'L':
                direction = (direction + 1) % TOTAL_DIRECTIONS
            elif inst == 'R':
                direction = (direction - 1) % TOTAL_DIRECTIONS
        return (direction_steps[0] == direction_steps[2] and direction_steps[1] == direction_steps[3] or direction != 0)