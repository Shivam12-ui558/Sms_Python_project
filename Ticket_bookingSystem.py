ticket_list = list(range(1, 51))

while True:
    print("Main Menu".center(35))
    print("""\t1. Book Ticket
    2. Show available seats
    3. Cancel ticket
    4. Exit""")

    try:
        choice = int(input('Choose operation from the above list : '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            ticket_number = int(input('Enter ticket number to book : '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 1 <= ticket_number <= 50:
            print('Invalid ticket number')
        elif ticket_list[ticket_number - 1] == 'Bb':
            print('Sorry! The ticket has been already booked!')
        else:
            ticket_list[ticket_number - 1] = 'Bb'
            print('Your ticket has been Booked!')

    elif choice == 2:
        print('===================== Available Seats =====================')
        for i, seat in enumerate(ticket_list, start=1):
            print(f"{seat}".center(5), end=' ')
            if i % 10 == 0:
                print()
        print('==========================================================')

    elif choice == 3:
        try:
            cancel_number = int(input('Enter ticket number to cancel : '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 1 <= cancel_number <= 50:
            print('Enter a valid ticket number')
        elif ticket_list[cancel_number - 1] == 'Bb':
            ticket_list[cancel_number - 1] = cancel_number
            print('Ticket has been successfully canceled')
        else:
            print("Ticket not found in bookings; cancellation can't be done")

    elif choice == 4:
        break

    else:
        print('Enter a valid choice')
