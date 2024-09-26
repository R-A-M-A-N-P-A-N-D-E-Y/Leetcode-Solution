class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if self.checkbooking(start, end):
            self.booked.append([start, end])
            return True
        else:
            return False
    
    def checkbooking(self, start: int, end: int) -> bool:
        for i, j in self.booked:
            if (start >= i and start < j) or (end > i and end <= j):
                return False
            if i > start and j < end:
                return False    
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)