'''
Problem Statement :
    A railway coach has seats represented as follows:
     
 Requirements Create the following functions: 
    1. count_seats(seats) 
    Returns the number of booked and available seats. 

    2. first_available(seats) 
    Returns the seat number of the first available seat. 

    3. occupancy_percentage(seats) 
    Returns the percentage of occupied seats. 

    4. display_available_seats(seats) 
    Displays all available seat numbers.       '''

def count_seats(seats):
    #Returns the number of booked and available seats.
    booked_count = seats.count("Booked")
    available_count = seats.count("Available")
    return booked_count, available_count

def first_available(seats):
    #Returns the seat number of the first available seat.
    if "Available" in seats:
        return seats.index("Available") + 1
    return None

def occupancy_percentage(seats):
    #Returns the percentage of occupied seats.
    total_seats = len(seats)
    if total_seats == 0:
        return 0.0
    
    booked_count = seats.count("Booked")
    occupancy = (booked_count / total_seats) * 100
    return occupancy

def display_available_seats(seats):
    #Displays all available seat numbers.
    available_seats = []
    for i in range(len(seats)):
        if seats[i] == "Available":
            available_seats.append(i + 1)
    
    print("Available seat numbers:", available_seats)
    return available_seats

# Main program
if __name__ == "__main__":
    seats = [
        "Booked", "Available", "Booked", "Booked",
        "Available", "Available", "Booked", "Available",
        "Booked", "Booked", "Available", "Booked"
    ]
    
    print("Seat Status List:", seats)
    print("-" * 50)
    
    # 1. Count seats
    booked, available = count_seats(seats)
    print(f"1. Count Seats:")
    print(f"   Booked seats: {booked}")
    print(f"   Available seats: {available}")
    print()
    
    # 2. First available seat
    first_avail = first_available(seats)
    print(f"2. First Available Seat:")
    print(f"   Seat number: {first_avail}")
    print()
    
    # 3. Occupancy percentage
    occupancy = occupancy_percentage(seats)
    print(f"3. Occupancy Percentage:")
    print(f"   {occupancy:.2f}%")
    print()
    
    # 4. Display all available seats
    print(f"4. Display Available Seats:")
    display_available_seats(seats)