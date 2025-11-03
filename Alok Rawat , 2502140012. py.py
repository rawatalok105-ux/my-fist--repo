#name - ALOK RAWAT , ENROLLMENT NO - 2502140012
# HOTEL MANAGEMENT SYSTEM
rooms = []              # List of rooms
guests = {}             # Dictionary for guests
occupied_rooms = set()  # Set of occupied rooms
ROOM_TYPES = ('Single', 'Double', 'Suite')  # Tuple of room types

# 1. LOGIN / PASSWORD PROTECTION

def login():
    PASSWORD = "admin123"
    while True:
        user_input = input("Enter password: ")
        if user_input == PASSWORD:
            print("Access granted.\n")
            main_menu()  #  Call main_menu()
            break
        else:
            print("Incorrect password. Try again.\n")


# 2. MAIN MENU (Called After Login)
def main_menu():
    while True:
        print("---- HOTEL MANAGEMENT MENU ----")
        print("1. Add Rooms")
        print("2. Add Guest")
        print("3. Modify Booking")
        print("4. Delete Guest")
        print("5. View Reports")
        print("6. Search Guest")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_rooms()
        elif choice == '2':
            add_guest()
        elif choice == '3':
            modify_booking()
        elif choice == '4':
            delete_guest()
        elif choice == '5':
            view_reports()
        elif choice == '6':
            search_guest()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# 3. ADD ROOMS
def add_rooms():
    n = int(input("Enter number of rooms to add: "))
    for _ in range(n):
        room_num = int(input("Enter room number: "))
        print("Select room type:")
        for i, t in enumerate(ROOM_TYPES, start=1):
            print(f"{i}. {t}")
        type_choice = int(input("Enter type (1/2/3): "))
        room_type = ROOM_TYPES[type_choice - 1]
        price = float(input("Enter price per night: "))

        rooms.append({
            'room_num': room_num,
            'type': room_type,
            'price': price,
            'is_available': True
        })
    print(f"\n{n} rooms added successfully!\n")


# 4. CORE FUNCTIONS

def add_guest():
    if not rooms:
        print("No rooms available! Please add rooms first.\n")
        return

    phone = input("Enter guest phone number: ")
    if phone in guests:
        print("Guest already exists.\n")
        return

    name = input("Enter guest name: ")
    room_num = int(input("Enter room number to book: "))

    # Check room availability
    for room in rooms:
        if room['room_num'] == room_num:
            if not room['is_available']:
                print("Room is already occupied!\n")
                return
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            guests[phone] = {'name': name, 'room_num': room_num, 'check_in': check_in}
            room['is_available'] = False
            occupied_rooms.add(room_num)
            print(f"Guest {name} booked Room {room_num} successfully!\n")
            return
    print("Room not found./n")


def modify_booking():
    phone = input("Enter guest phone number to modify: ")
    if phone not in guests:
        print("Guest not found.\n")
        return

    new_room = int(input("Enter new room number: "))
    # Check if room exists and available
    room_exists = any(room['room_num'] == new_room for room in rooms)
    if not room_exists:
        print("Room not found.\n")
        return
    if new_room in occupied_rooms:
        print("That room is already occupied!\n")
        return

    old_room = guests[phone]['room_num']
    guests[phone]['room_num'] = new_room
    occupied_rooms.discard(old_room)
    occupied_rooms.add(new_room)

    for room in rooms:
        if room['room_num'] == old_room:
            room['is_available'] = True
        if room['room_num'] == new_room:
            room['is_available'] = False

    print("Booking updated successfully.\n")


def delete_guest():
    phone = input("Enter guest phone number to delete: ")
    if phone in guests:
        room_num = guests[phone]['room_num']
        del guests[phone]
        occupied_rooms.discard(room_num)
        for room in rooms:
            if room['room_num'] == room_num:
                room['is_available'] = True
        print("Guest record deleted successfully.\n")
    else:
        print("Guest not found.\n")


# 5. REPORTS AND SEARCH
def view_reports():
    print("\n--- Current Guests Report ---")
    if not guests:
        print("No guests found.\n")
    else:
        for phone, info in guests.items():
            print(f"Name: {info['name']}, Phone: {phone}, Room: {info['room_num']}, Check-in: {info['check_in']}")
    print("\nOccupied rooms:", occupied_rooms)
    print()


def search_guest():
    keyword = input("Enter guest name or phone number: ")
    found = False
    for phone, info in guests.items():
        if keyword.lower() in info['name'].lower() or keyword == phone:
            print(f"Found: {info['name']} | Room {info['room_num']} | Check-in {info['check_in']}")
            found = True
    if not found:
        print("No matching guest found.\n")
# 6. MAIN EXECUTION FLOW

if __name__ == "__main__":
    login()
