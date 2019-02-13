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

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        face = 0
        iStart = jStart = 0
        self.dfs(robot, iStart, jStart, face, visited)
    
    def dfs(self, robot, i, j, face, visited):
        robot.clean()
        visited.add((i,j))
        faceNew = face
        for _ in range(4):
            robot.turnRight()
            # next facing direction
            faceNew = (faceNew + 1) % 4
            # next position
            iNew = i + faceNew - 1 if faceNew % 2 == 0 else i
            jNew = j - faceNew + 2 if faceNew % 2 == 1 else j
            if (iNew, jNew) not in visited and robot.move():
                self.dfs(robot, iNew, jNew, faceNew, visited) 
        # go back to where it came from
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()