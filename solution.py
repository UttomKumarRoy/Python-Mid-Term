class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = ()
        self.initializer()
        self.entry_hall(self)

    def initializer(self):
        for row in range(1, self.rows + 1):
            self.seats[row] = ['O' for col in range(self.cols)]
        
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        y=list(self.show_list)
        y.append(show_info)
        self.show_list=tuple(y)
        self.seats[id] = [['O' for col in range(self.cols)] for row in range(self.rows)]

    def book_seats(self, show_id, seat_list):
        if show_id in self.seats:
            for row, col in seat_list:
                if 1 <= row <= self.rows and 1 <= col <= self.cols:
                    if self.seats[show_id][row - 1][col - 1] == 'O':
                        self.seats[show_id][row - 1][col - 1] = 'X'
                        print(f"Seat ({row}, {col}) booked for show Id {show_id}.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked for show Id {show_id}.")
                else:
                    print(f"Invalid seat ({row}, {col}) for show Id {show_id}.")

        else:
            print(f"Show Id {show_id} not found.")

    def view_show_list(self):
        print("Show List:")
        for id, movie_name, time in self.show_list:
            print(f"Show ID: {id}, Movie Name: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"Available seats for show ID {show_id}:")
            for row in range(1, self.rows + 1):
                for col in range(1, self.cols + 1):
                    if self.seats[show_id][row - 1][col-1] == 'O':
                        print(f"Seat ({row}, {col})")
        else:
            print(f"Show Id {show_id} not found.")

hall = Hall(5, 10, 1)
hall.entry_show(111, "100% LOVE", "10:00 AM")
hall.entry_show(222, "Gerilla", "08:00 AM")

print("Welcome to Star Cinema World")

while True:
    print("1. VIEW ALL SHOW TODAY ")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Entry New Show")
    print("5. EXIT")

    ch=int(input("ENTER OPTION:"))
    if ch==1:
        hall.view_show_list()
    elif ch==2:
        a=int(input("Enter Show Id:"))
        hall.view_available_seats(a)

    elif ch==3:
        a=int(input("Enter show_id:"))
        print("Enter number of seats you want to book:")
        n=int(input())
        nt=n
        seat_list=[]
        count=1
        while n:
            print(f"Seat {count} Info:")
            count=count+1
            r=int(input("Enter Seat Row:"))
            c=int(input("Enter Seat Col:"))
            t=(r,c)
            n=n-1
            seat_list.append(t)
        hall.book_seats(a, seat_list)
    
    elif ch==4:
        a=int(input("Enter Show Id:"))
        b=input("Enter Movie Name:")
        c=input("Enter Show Time:")
        hall.entry_show(a, b, c)

    elif ch==5:
        exit()
    else:
        print("Invalid Option!!! Enter valid option please.")
        