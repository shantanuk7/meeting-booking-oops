from SmallRoom import SmallRoom
from LargeRoom import LargeRoom

class main:
    def __init__(self):
        small_room = SmallRoom("Small Room 1")
        large_room = LargeRoom("Large Room 1")
        while True:
            print("Welcome to Meeting Room Booking System\n")

            print("Select Room Type:")
            print("1. Small Room")
            print("2. Large Room")
            print("3. Exit")

            choice = input("Enter your choice:")

            if choice == "1":
                selected_room = small_room
            elif choice == "2":
                selected_room = large_room
            elif choice == "3":
                exit()
            else:
                print("Invalid choice")
                exit()

            print("\nAvailable Time Slots:")

            available_slots = []

            for hour in range(9, 18):
                if selected_room.is_available(hour):
                    available_slots.append(hour)
                    print(f"{hour}:00 - {hour+1}:00")

            if not available_slots:
                print("No slots available")
                exit()

            # Time Slot selection
            slot = int(input("\nEnter starting hour to book (e.g., 9 for 9–10): "))

            if selected_room.book_room(slot):
                print("\nBooking Confirmed!")
                print("Room:", selected_room.name)
                print(f"Time: {slot}:00 - {slot+1}:00")
                print("Price:", selected_room.price_per_hour())
            else:
                print("\nSorry, that time slot is already booked.")

if __name__ == "__main__":
    main()  