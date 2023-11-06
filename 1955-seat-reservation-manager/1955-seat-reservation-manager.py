class SeatManager:
    def __init__(self, n):
        if n <= 0:
            raise ValueError("Invalid value of n.")
        self.seats = list(range(1, n + 1))

    def reserve(self):
        if not self.seats:
            return -1 
        
        reserved_seat = heapq.heappop(self.seats) 
        return reserved_seat

    def unreserve(self, seat_number):
        if seat_number > 0:
            heapq.heappush(self.seats, seat_number) 