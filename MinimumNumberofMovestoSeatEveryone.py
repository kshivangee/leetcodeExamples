class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        minmoves=0
        seats.sort()
        students.sort()
        for i in range(len(students)):
            minmoves += (abs(students[i]-seats[i]))
        return minmoves