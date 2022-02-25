# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self):
        self.moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
        self.visited = set()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0)
        
    def dfs(self, robot, i, j, direction):
        self.visited.add((i, j))
        robot.clean()
        ni, nj = i + self.moves[direction][0], j + self.moves[direction][1]
        new_dir = direction
        for _ in range(len(self.moves)):
            ni, nj = i + self.moves[new_dir][0], j + self.moves[new_dir][1]
            if (ni, nj) not in self.visited and robot.move():
                self.dfs(robot, ni, nj, new_dir)
            new_dir = (new_dir + 1) % len(self.moves)
            robot.turnRight()
        # backtracking - returning from where it came
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        