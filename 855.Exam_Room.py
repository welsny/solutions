class ExamRoom:
    def __init__(self, N: int):
        self.dists = [0]*N
        self.seats = [False]*N

    def update_seats(self):
        d = float('inf')
        for i, s in enumerate(self.seats):
            if s:
                d = 0
            else:
                d += 1
            self.dists[i] = d
            
        d = float('inf')
        for i, s in enumerate(reversed(self.seats)):
            if s:
                d = 0
            else:
                d += 1
            self.dists[-1-i] = min(self.dists[-1-i], d)

    def seat(self) -> int:
        i = self.dists.index(max(self.dists))
        self.seats[i] = True
        self.update_seats()
        return i

    def leave(self, p: int) -> None:
        self.seats[p] = False
        self.update_seats()



    def __init__(self, N: int):
        self.N = N
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        
        curr_max = 0
        curr_i = 0
        
        if self.seats[0]:
            curr_max = self.seats[0]
            curr_i = 0

        for i, (s, s2) in enumerate(zip(self.seats, self.seats[1:])):
            dist = (s2-s)//2
            if dist > curr_max:
                curr_max = dist
                curr_i = s+dist
            
        if self.seats[-1] != self.N-1:
            dist_from_back = self.N-1-self.seats[-1]
            if dist_from_back > curr_max:
                curr_max = dist_from_back
                curr_i = self.N-1

        self.seats.append(curr_i)
        self.seats.sort()
        return curr_i

    def leave(self, p: int) -> None:
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)